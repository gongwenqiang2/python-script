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
    print data.ix['Colorado',['two','three']]
    print data.ix[['Colorado','Utah'],[3,0,1]]
    print data.ix[:'Utah','two']
    print data.ix[data.three>5,:3]
# pd_dataframe01()

def pd_01():
    s1=Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
    s2=Series([-2.1,3.6,-1.5,4,3.6],index=['a','c','e','f','g'])
    print s1
    print s2
    print s1+s2
# pd_01()

def pd_02():
    frame=DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),index=['Ohio', 'Colorado', 'Utah', 'New York'])
    print frame
    series=frame.ix[0]
    print series
    print frame-series
    series2=Series(range(3),index=['b','e','f'])
    print frame+series2
    series3=frame['d']
    print series3
    print frame.sub(series3,axis=0)
# pd_02()

def pd_03():
    frame=DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Ohio', 'Colorado', 'Utah', 'New York'])
    print frame
    print np.abs(frame)
    f=lambda x:x.max()-x.min()
    print frame.apply(f)
    print frame.apply(f,axis=1)
    def f(x):
        return Series([x.min(),x.max()],index=['min','max'])
    print frame.apply(f)
    format=lambda x:'%.2f' % x
    print frame.applymap(format)
# pd_03()


def pd_04():
    obj=Series(range(4),index=['d','a','b','c'])
    print obj
    print obj.sort_index()
    frame=DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
    print frame.sort_index()
    print frame.sort_index(axis=1)
    print frame.sort_index(ascending=False)
    obj1=Series([4,7,-3,2])
    print obj1.order()
    print frame.sort_index(by='b')
    print frame.sort_index(by=['a','b'])
    print frame.describe()
# pd_04()

def pd_05():
    obj=Series([7,-5,7,4,2,0,4])
    print obj.rank()
    print obj.rank(method='first')
    print obj.rank(ascending=False,method='first')
    print obj.describe()
# pd_05()

def pd_06():
    import pandas.io.data as web
    all_data={}
    for ticker in ['APPL','IBM','MSFT','GOOG']:
        all_data[ticker]=web.get_data_yahoo(ticker,'1/1/2000','1/1/2010')
    print all_data
pd_06()