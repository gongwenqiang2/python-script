# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import math
from sklearn.cross_validation import train_test_split


#name columns
columns=['sepal_length ','sepal_width','petal_length','petal_width','species']
# get data
try:
    data=DataFrame(pd.read_csv(u'D:\git\python-script\data_mining_learn\knn_learn_python\iris.data.csv',header=None))
except:
    data=DataFrame(pd.read_csv(u'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None))
data.columns=columns
print data[-1:]

#get sample and test data
def split_dataset(dataset,bin):
    sampler=np.random.permutation(len(dataset))
    random_data=dataset.reindex(sampler)
    train_data=random_data[:int(len(dataset)*bin)]
    test_data=random_data[int(len(dataset)*bin):]
    return train_data,test_data

train_data,test_data=split_dataset(dataset=data,bin=0.7)

#entropy calculate function
def calc_entropy(s):
    s_len=len(s)
    label_counts=s.value_counts()
    label_p=label_counts/s_len
    print label_p
    entropy=-sum(map(lambda x:x*(math.log(x,2)),label_p.values))
    return entropy

entropy=calc_entropy(train_data.species)
print entropy





