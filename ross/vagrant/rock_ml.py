import sqlite3
import random
import h5py
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes, LogisticRegressionWithSGD
from pyspark.rddsampler import RDDSamplerBase

class RDDRangeSampler(RDDSamplerBase):
	def __init__(self, lowerBound, upperBound, seed=None):
		RDDSamplerBase.__init__(self, False, seed)
		self._lowerBound = lowerBound
		self._upperBound = upperBound
	def func(self, split, iterator):
		self._random = random.Random(self._seed ^ split)
		# mixing because the initial seeds are close to each other
		for _ in range(10):
			self._random.randint(0, 1)
		for obj in iterator:
			if self._lowerBound <= self._random.random() < self._upperBound:
				yield obj

def randomSplit(rdd, weights, seed=None):
	s = float(sum(weights))
	cweights = [0.0]
	for w in weights:
		cweights.append(cweights[-1] + w / s)
	if seed is None:
		seed = random.randint(0, 2 ** 32 - 1)
	return [rdd.mapPartitionsWithIndex(RDDRangeSampler(lb, ub, seed).func, True) for lb, ub in zip(cweights, cweights[1:])]


dbpath = '/vagrant/MillionSongSubset/AdditionalFiles/'
# Get list of songs with mbtags, artist, and independent vars

## Get artist mbtags from subset_artist_term.db (table = artist_mbtag)
dbname ='subset_artist_term.db'

with sqlite3.connect(dbpath+dbname) as conn:
	c = conn.cursor()
	c.execute("SELECT artist_id, mbtag FROM artist_mbtag")
	artistTags = sc.parallelize(c.fetchall())


# group tags by artist
artistTagList = artistTags.groupByKey()
artistTagList.take(3)

# check if rock in group tag or not
artistRocks = artistTagList.map(lambda (ar, tags): (ar, float(sum(['rock' in tag for tag in tags]) > 0)))
artistRocks.take(3)


# merge song with artist

## Match artist to track using subset_track_metadata.db (table = songs)

dbname ='subset_track_metadata.db'

with sqlite3.connect(dbpath+dbname) as conn:
	c = conn.cursor()
	c.execute("SELECT artist_id, track_id FROM songs")
	trackArtist = sc.parallelize(c.fetchall())

trackArtist.take(3)

trackRocks = trackArtist.leftOuterJoin(artistRocks).map(lambda (ar, (tr, rocks)): (tr, rocks))
trackRocks.take(3)

# get song data and merge

## Get song data from subset_msd_summary_file.h5[analysis][songs]
file_name = 'subset_msd_summary_file.h5'
#songData = sc.parallelize(list(h5py.File(dbpath+file_name, 'r')['analysis']['songs'][:]))
songData = sc.parallelize(list(h5py.File(dbpath+file_name, 'r')['analysis']['songs'][:])).map(lambda x: (x[30], (x[3], x[4], x[21], x[23], x[24], x[27], x[28])))
songData.take(3)

allData = trackRocks.join(songData).map(lambda (tr, (rocks, data)): (tr, (0.0 if rocks is None else rocks, data)))
allData.take(3)

# label data
labeledData = allData.map(lambda (tr, (rocks, data)): LabeledPoint(rocks, [x for x in data]))
labeledData.take(3)

# split data
trainData, testData = randomSplit(labeledData, [0.7, 0.3])

# train model
model = LogisticRegressionWithSGD.train(trainData)

# evaluate model
labelsAndPreds = testData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(testData.count())
print("Test Error = " + str(trainErr))







