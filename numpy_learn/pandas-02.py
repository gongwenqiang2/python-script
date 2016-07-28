# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

def pd_series01():
    obj=Series(np.arange(4.),index=('a','b','c','d'))
    print obj
    print obj['b']
    print obj[1]
    print obj[2:4]
    print obj[['b','b','d']]
    print obj[[1,3]]
    print obj[obj<2]
    print obj['a':'c']
    obj['a':'c']=5
    print obj
# pd_series01()

def pd_dataframe01():
    data = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])
    print data
    print data['two']
    print data[['three','one']]
    print data[:2]
    print data[data['three']>5]
    print data<5
pd_dataframe01()