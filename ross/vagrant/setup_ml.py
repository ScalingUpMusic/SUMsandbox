import sqlite3
import random
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

## Match track to song data in subset_msd_summary_file.h5[analysis][songs]


# Flatten list of songs to repeat for each tag

# Split list of songs in to train and test based on Artists

# Train Model

# Test Model