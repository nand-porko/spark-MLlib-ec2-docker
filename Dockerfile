from gcr.io/datamechanics/spark:platform-3.2.1-latest
# from gcr.io/datamechanics/spark:3.1.2-hadoop-3.2.0-java-8-scala-2.12-python-3.8-dm17

# RUN apk --update add wget tar bash coreutils procps openssl
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3

# Set python3.7 as the default python
# RUN update-alternatives --set python /usr/bin/python3
# Set env variables
ENV DAEMON_RUN=true
ENV SPARK_VERSION=3.1.3
ENV HADOOP_VERSION=3.2
ENV SCALA_VERSION=2.12.3
ENV SCALA_HOME=/usr/share/scala
ENV SPARK_HOME=/spark
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip

# Get Apache Spark
# RUN wget http://mirror.ox.ac.uk/sites/rsync.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# RUN tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
#     mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /spark && \
#     rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
#     export PATH=$SPARK_HOME/bin:$PATH
# RUN apk update
# RUN apk add python3

COPY Cloud_prediction.py ./
COPY model123 model123
#COPY ValidationDataset.csv ./
COPY requirements.txt ./
RUN pip3 install --upgrade pip --user
RUN pip3 install numpy pandas seaborn matplotlib Jinja2 pyspark==3.1.2 --user
RUN echo "export SPARK_HOME="../"" >> ~/.bashrc
RUN source ~/.bashrc
# ENTRYPOINT ['python']

