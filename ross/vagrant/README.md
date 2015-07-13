# Some Notes on Setting Up Vagrant & Spark

http://thegrimmscientist.com/2014/12/01/vagrant-tutorial-spark-in-a-vm/

## Vagrant

Download a premade box

	vagrant box add <somename> <url-to-download-from>
	vagrant box add precise32 http://files.vagrantup.com/precise32.box

Output

	==> box: Adding box 'precise32' (v0) for provider: 
    	box: Downloading: http://files.vagrantup.com/precise32.box
	==> box: Successfully added box 'precise32' (v0) for 'virtualbox'!

To check which boxes are available

	vagrant box list

Initialize a box (in final project sandbox SUMsandbox/ross/vagrant):
	
	vagrant init precise32

Then start the box in the same directory as the Vagrantfile created by the previous command

	vagrant up


Get on to your vm

	vagrant ssh

## Spark

Install a JDK

	sudo apt-get -y update
	sudo apt-get -y install openjdk-7-jdk

Download & extract Spark

	wget http://d3kbcqa49mib13.cloudfront.net/spark-1.1.0-bin-hadoop1.tgz
	tar -zxf spark-1.1.0-bin-hadoop1.tgz

cd to Spark
	
	cd spark-1.1.0-bin-hadoop1

### In Scala

Run Spark Shell

	./bin/spark-shell

Test Spark shell

	scala> val textFile = sc.textFile("README.md")
	scala> textFile.count()

### In Python

Run Spark shell

	./bin/pyspark

Test Spark shell

	>>> textFile = sc.textFile("README.md")
	>>> textFile.count()

## "Transfer" a file

Open a new terminal window, from your "local" machine in the directory with Vagrantfile, create a test text file

	echo "some test text \n here" > test.txt

On your vagrant vm you should now see this test.txt (do no have to restart machine or anything, it's just there)

	vagrant@precise32:/$ cd /vagrant
	vagrant@precise32:/vagrant$ ls
	README.md  test.txt  Vagrantfile

On your vagrant vm copy test.txt to your spark directory

	cp /vagrant/test.txt /home/vagrant/spark-1.1.0-bin-hadoop1

Re-run Spark shell and check test.txt
	
	./bin/pyspark
	>>> textFile = sc.textFile("test.txt")
	>>> textFile.count()
	2

# Million Song Data Set

The million song data set uses HDF5 files. There is a python library "h5py" that handles those. Here is a link for using that library to turn .h5 files in to RDDs.

https://hdfgroup.org/wp/2015/03/from-hdf5-datasets-to-apache-spark-rdds/

(TODO: Later we could probably put all this in a Vagrant file to install on machine build)

SO we need to install h5py, so we need to install pip

	sudo apt-get install python-pip
	pip install h5py
