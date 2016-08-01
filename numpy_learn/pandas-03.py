# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

def pd_01():
    obj=Series(['c','a','d','a','a','b','c'])
    uniques=obj.unique()
    print uniques
    print uniques.sort()
    print pd.value_counts(obj,sort=False)
    mask=obj.isin(['b','c'])
    print mask
    print obj[mask]
# pd_01()

def pd_02():
    string_data=Series(['a','b','c',np.nan,'e',None])
    print string_data
    print string_data.isnull()
    print string_data.dropna()
    df=DataFrame(np.random.randn(7,3))
    df.ix[:4,1]=np.nan
    df.ix[:2,2]=np.nan
    print df
    print df.dropna()
    print df.fillna(0)
    print df.fillna({1:0.5,3:-1})
    print df
    df.fillna(0,inplace=True)
    print df
# pd_02()

def pd_03():
    df=DataFrame(np.random.randn(6,3))
    df.ix[2:,1]=np.nan
    df.ix[4:,2]=np.nan
    print df
    print df.fillna(method='ffill')
    print df.fillna(method='ffill',limit=2)
    data=Series([1.,None,3.5,None,7])
    print data.fillna(data.mean())
    print df.fillna(df.mean())
pd_03()