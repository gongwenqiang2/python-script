# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import DataFrame,Series

def merge_data01():
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                      'data1': range(7)})
    df2 = DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
    print df1
    print df2
    print pd.merge(df1,df2,on='key')
    df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                      'data1': range(7)})
    df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
    print pd.merge(df3,df4,left_on='lkey',right_on='rkey')
    left=DataFrame({'key1':['foo','foo','bar'],'key2':['one','two','three'],'lval':[1,2,3]})
    right=DataFrame({'key1':['foo','foo','bar','bar'],'key2':['one','two','one','two'],'rval':[4,5,6,7]})
    print pd.merge(left,right,on=['key1','key2'],how='outer')
# merge_data01()

def merge_data02():
    lefth=DataFrame({'key1':['ohio','ohio','ohio','nevada','nevada'],'key2':[2000,2001,2002,2001,2002],'data':np.arange(5)})
    righth=DataFrame(np.arange(12).reshape((6,2)),index=[['neveda','neveda','ohio','ohio','ohio','ohio'],[2001,2000,2000,2000,2001,2002]],columns=['event1','event2'])
    print lefth
    print righth
    print pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True)
merge_data02()