import sys
import os.path
import subprocess
import h5py
import numpy as np

from random import random

from pyspark import SparkContext, SparkConf
from pyspark.mllib.clustering import KMeans, KMeansModel



k_clusters = 50
target_shape = 10000
max_size = 0

k_means_data = []


print "Collecting timbre data..."
file_list = subprocess.check_output(['/usr/bin/find', '/vagrant/MillionSongSubset/data', '-name', '*.h5', '-print'])

for file_name in file_list.split("\n"):
    # Skip directories or other non-files
    if not os.path.isfile(file_name):
        continue
    
    # Convert timbre data to 1-dimensional input for K-means
    h5_file = h5py.File(file_name, 'r')
    file_val = np.array(h5_file['analysis/segments_timbre'])
    
    # Make it 1-dimensional
    file_val = file_val.reshape(file_val.shape[0] * file_val.shape[1])[0:target_shape]
    
    # Pad so all songs have same length of features
    file_val = np.pad(file_val, (0, target_shape - file_val.shape[0]), 'constant', constant_values=(0.0,0.0))
    
    # Add to actual feature array
    k_means_data.append(file_val)
    
    h5_file.close()



print("%s total files read...") % len(k_means_data)

sc = SparkContext(appName="W251")

print "Parallelizing data stream..."
k_means_rdd = sc.parallelize(k_means_data)

print "Training K-Means model..."
model = KMeans.train(k_means_rdd, k_clusters, maxIterations=10, runs=10, initializationMode="random")

print "Serializing model to disk..."
model.save(sc, "./temp_model.smd")

sc.stop()

print "Done."