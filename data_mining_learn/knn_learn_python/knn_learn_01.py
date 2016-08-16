# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import math

#name columns
columns=['sepal_length ','sepal_width','petal_length','petal_width','species']
#get data
data=DataFrame(pd.read_csv(u'E:\学习\数据挖掘\数据挖掘学习实践\python实现KNN分类算法\iris.data.csv',header=None))
data.columns=columns
print data[:5]

#get sample and test data
sampler=np.random.permutation(len(data))
random_data=data.reindex(sampler)
sample_data=random_data[:int(len(data)*0.7)]
test_data=random_data[int(len(data)*0.7):]

#distance func
def get_distance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance +=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)
data1=[2,2,2,'a']
data2=[4,4,4,'b']
print get_distance(data1,data2,3)

