import sqlite3
import random
import h5py
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes
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

# Get list of Artists
## get from subset_artist_term.db (table = artists)
dbname ='subset_artist_term.db'

with sqlite3.connect(dbpath+dbname) as conn:
	c = conn.cursor()
	c.execute("SELECT artist_id FROM artists")
	distTable = sc.parallelize(c.fetchall())

# Split Artists in to test and train
trainArtists, testArtists = randomSplit(distTable, [0.7, 0.3])

trainArtists.take(3)
testArtists.take(3)

# Get list of songs with mbtags, artist, and independent vars

## Get artist mbtags from subset_artist_term.db (table = artist_mbtag)
dbname ='subset_artist_term.db'

with sqlite3.connect(dbpath+dbname) as conn:
	c = conn.cursor()
	c.execute("SELECT artist_id, mbtag FROM artist_mbtag")
	artistTags = sc.parallelize(c.fetchall())



artistTags.take(3)

## Match artist to track using subset_track_metadata.db (table = songs)

dbname ='subset_track_metadata.db'

with sqlite3.connect(dbpath+dbname) as conn:
	c = conn.cursor()
	c.execute("SELECT track_id, artist_id FROM songs")
	trackArtist = sc.parallelize(c.fetchall())

trackArtist.take(3)

artistTrackTag = trackArtist.map(lambda (x,y): (y, x)).leftOuterJoin(artistTags)
artistTrackTag.take(3)

#[
# (u'AR6U6C51187B9B6F68', (u'TRASTIS128F92FA998', u'classical')),
# (u'AR6U6C51187B9B6F68', (u'TRAGXBC128F148E5CC', u'classical')),
# (u'ARZWK2R1187B98F09F', (u'TRARANL128F1478789', u'hardcore punk'))
#]

## Match get song data from subset_msd_summary_file.h5[analysis][songs]
file_name = 'subset_msd_summary_file.h5'
#songData = sc.parallelize(list(h5py.File(dbpath+file_name, 'r')['analysis']['songs'][:]))
songData = sc.parallelize(list(h5py.File(dbpath+file_name, 'r')['analysis']['songs'][:])).map(lambda x: (x[30], (x[3], x[4], x[21], x[23], x[24], x[27], x[28])))
songData.take(3)

# 30 = track_id

# 3 = duration
# 4 = danceability
# 21 = key
# 23 = loudness
# 24 = mode
# 27 = tempo
# 28 = time_signature

# match track to song data
allData = artistTrackTag.map(lambda (ar,(tr, tag)): (tr,(ar,tag))).leftOuterJoin(songData).map(lambda (tr, ((ar, tag),data)): (ar, (tr, tag, data)))
allData.take(3)

# Split list of songs in to train and test based on Artists
# Had a hard time doing this, just splitting songs for now:
trainData, testData = randomSplit(allData.map(lambda (ar, (tr, tag, data)):(tag, data)), [0.7, 0.3])
trainData.take(3)
testData.take(3)

# Train Model
model = NaiveBayes.train(trainData.map(lambda (tag,data): LabeledPoint(tag, [x for x in data])))

# Test Model

