import sqlite3

dbpath = '/vagrant/MillionSongSubset/AdditionalFiles/'

#dbname = 'subset_artist_similarity.db'
#dbname = 'subset_artist_term.db'
dbname ='subset_track_metadata.db'

conn = sqlite3.connect(dbpath+dbname)

# i = 0
# for x in conn.iterdump():
# 	i+=1
# 	print(x)
# 	if i > 10:
# 		break

c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = c.fetchall()

for table in tables:
	print('\n##############################')
	print('Table: %s' % table[0])
	c.execute("SELECT * FROM %s LIMIT 10;" % (table[0]))
	print([des[0] for des in c.description])
	for row in c.fetchall():
		print(row)

conn.close()



