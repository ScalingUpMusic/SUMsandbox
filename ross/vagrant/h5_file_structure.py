import h5py

def recursiveKeys(obj, space="", maxcount = 10):
	try:
		ks = obj.keys()
		for k in ks:
			print space+k
			recursiveKeys(obj[k], space=space+" ")
	except AttributeError:
		count = 0
		for x in obj:
			print space+str(x)
			count += 1
			if count >= maxcount:
				print space+'...('+str(len(obj))+')'
				break
		return



# file_name = '/vagrant/MillionSongSubset/data/A/K/W/TRAKWGL12903CB8529.h5'
#file_name = '/vagrant/MillionSongSubset/AdditionalFiles/subset_msd_summary_file.h5'
file_name = '/vagrant/MillionSongSubset/data/A/X/L/TRAXLZU12903D05F94.h5' 
h5_file = h5py.File(file_name, 'r')

recursiveKeys(h5_file)