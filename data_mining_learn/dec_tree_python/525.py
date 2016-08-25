
__author__ = 'gongwenqiang'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import math
from sklearn import tree




#name columns
columns=['sepal_length','sepal_width','petal_length','petal_width','species']
# get data
try:
    data=DataFrame(pd.read_csv(u'D:\git\python-script\data_mining_learn\knn_learn_python\iris.data.csv',header=None))
except:
    data=DataFrame(pd.read_csv(u'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None))
data.columns=columns

clf=tree.DecisionTreeClassifier()
print data.ix[:,0:4]

clf=clf.fit(data.ix[:,0:4],data['species'])

print clf
