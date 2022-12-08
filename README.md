# spark-MLlib-ec2-docker
This project will demonstrate how to run Apache Spark on multiple EC2 instances, connect to a Jupyter notebook, use Spark's MLlib to train machine learning models on cloud, create a docker container which can load the ML model and predict wine classifications.
## Creating a Spark Cluster on EC2
Assuming that you already have your AWS credentials and your AWS key-pair.
### Setting up the cluster
To create a spark cluster on EC2, we will use [flintrock](https://github.com/nchammas/flintrock). To install Flintrock:
```
pip3 install flintrock
```
Next, we will have to configure the Spark and Hadoop version to use in our cluster:
```
flintrock configure
```
We should also specify AWS key-pair name, and location in the configure file. We can also use the configure file to set the number of slaves required for our spark cluster.

Launch a Spark cluster with:
```
flintrock launch <cluster-name>
```
Once the cluster is successfully launched, we can login into the cluster:
```
flintrock login <cluster-name>
```
Now you will be logged into Spark MAster's EC2 instance.

### Adding dependancies for the project
We will install Jupyter notebook and its dependancines by installing Anaconda python distribution.
```
[SparkMaster] wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh
[SparkMaster] sh Anaconda2-4.2.0-Linux-x86_64.sh
```
The installation will ask if you would like to set the path variables, if not, add the path variable to the ~/.bashrc
```
[SparkMaster] export PATH=/home/user/path/to/anaconda2/bin:$PATH
```
Source the .bashrc file and quick test the jupyter notebook
```
jupyter notebook
```
### Setting up Jupyter notebook
Now we are going to run Jupyter with Pyspark. I put the following commands in a shell script ```jupyter_setup.sh```
```
export spark_master_hostname=SparkMasterPublicDNS
export memory=1000M 

PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS="notebook --no-browser --port=7777" pyspark --master spark://$spark_master_hostname:7077 --executor-memory $memory --driver-memory $memory
```
You can get the Spark Master Public DNS from your AWS console.
To tunnel your jupyter in SparkMaster to local, ```source jupyter_setup.sh```, from your local:
```
[LocalComputer] ssh -i ~/path/to/AWSkeypair.pem -N -f -L localhost:7776:localhost:7777 ec2-user@SparkMasterPublicDNS
```
The default user in Flintrock is ec2-user so that will work most of the time. Other common user name can be ```ubuntu```.

