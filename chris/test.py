import h5py

file_name = '/vagrant/MillionSongSubset/data/A/X/L/TRAXLZU12903D05F94.h5'
h5_file   = h5py.File(file_name, 'r')

print "Song Metadata:"
print "\tartist_mbid: %s" % h5_file['metadata/songs'][0][8]
print "\tartist_name: %s" % h5_file['metadata/songs'][0][9]
print "\tartist_playmeid: %s" % h5_file['metadata/songs'][0][10]
print "\trelease: %s" % h5_file['metadata/songs'][0][14]
print "\trelease_7digitalid: %s" % h5_file['metadata/songs'][0][15]
print "\tsong_hotttnesss: %s" % h5_file['metadata/songs'][0][16]
print "\tsong_id: %s" % h5_file['metadata/songs'][0][17]
print "\ttitle: %s" % h5_file['metadata/songs'][0][18]
print "\ttrack_7digitalid: %s" % h5_file['metadata/songs'][0][19]

for key in h5_file.keys():
	print "Subkeys (%s):" % key
	for subkey in h5_file[key].keys():
		print "\t%s: %s" % (subkey, h5_file[key][subkey])

