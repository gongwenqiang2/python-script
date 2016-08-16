# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import math


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
print get_distance(data.ix[1],data.ix[2],3)

def sort_cut_data(df,k,column='distance'):
    sort_data=df.sort_values(by=column)
    return sort_data[:k]

# print sort_cut_data([2,1,5],2)

def get_neighbors(s_set,t_set,k):
    neighbors_list=[]
    for t in t_set.index:
        for s in s_set.index:
            distance=get_distance(test_data.ix[t],sample_data.ix[s],3)
            neighbors_list.append([t,s,distance,sample_data.ix[s,4]])
    neighbors_df=DataFrame(neighbors_list,columns=['t_index','s_index','distance','s_species'])
    neighbors_cut=neighbors_df.groupby('t_index',as_index=False).apply(sort_cut_data,k=k,column='distance')
    return neighbors_cut

neighbors=get_neighbors(sample_data,test_data,5)
print neighbors[:10]

def top(df,n=1,column='pre_rank'):
    df_sorted=df.sort_values(by=column)
    return df_sorted[-n:]

def get_pre_species(neighbors):
    grouped=neighbors.groupby(['t_index','s_species'],as_index=False)['distance'].agg({'pre_rank':'sum'})
    return grouped.groupby('t_index',as_index=False).apply(top,n=1).reset_index().drop(['level_0','level_1'],axis=1)
pre_species=get_pre_species(neighbors)
# print pre_species.sort_values(by='t_index')



test_data['t_index']=test_data.index

compare_data=pd.merge(left=pre_species,right=pre_species,how='left',left_on='t_index',right_on='t_index')
print compare_data['s_species_x']==compare_data['s_species_y']



