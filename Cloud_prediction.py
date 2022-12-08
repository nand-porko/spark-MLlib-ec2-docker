#!/usr/bin/env python
# coding: utf-8

# In[1]:

print("Welcome")
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #plotting
import seaborn as sns #good visualizing
import os
import warnings
warnings.filterwarnings('ignore')


# In[2]:


from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark import SparkContext
sc = SparkContext('local')
spark = SparkSession.builder.appName('Porko').getOrCreate()
print("XXXXXXXXXXXXX----------->Spark loaded")

# In[3]:


# path = "TrainingDataset.csv"
validation_path = "ValidationDataset.csv"
# data = spark.read.option("delimiter", ";").option("header", "true").option("inferSchema","true").csv(path)
validation_data = spark.read.option("delimiter", ";").option("header", "true").option("inferSchema","true").csv(validation_path)

print("XXXXXXXXXXXXX----------->data   loaded")
# In[4]:


feature_list = ['fixed acidity',
 'volatile acidity',
 'citric acid',
 'residual sugar',
 'chlorides',
 'free sulfur dioxide',
 'total sulfur dioxide',
 'density',
 'pH',
 'sulphates',
 'alcohol']


# In[10]:


from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler
validation_assembler = VectorAssembler(inputCols=feature_list,outputCol="corr_features")
df_validation = validation_assembler.transform(validation_data)
# df_validation.show()


# In[6]:


from pyspark.ml.classification import RandomForestClassificationModel

rf = RandomForestClassificationModel.load("./model123")

print("XXXXXXXXXXXXX----------->model loaded")
# In[7]:


predictions = rf.transform(df_validation)


# In[8]:


from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="quality", predictionCol="prediction")
accuracy = evaluator.evaluate(predictions)
print("Accuracy = %s" % (accuracy))
print("Test Error = %s" % (1.0 - accuracy))


# In[9]:


predictions.select('quality', 'prediction', 'probability').show()
print("the end")

# In[ ]:




