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
# merge_data02()

def merge_data03():
    arr=np.arange(12).reshape(3,4)
    print arr
    print np.concatenate([arr,arr],axis=1)
    print np.concatenate([arr,arr],axis=0)
# merge_data03()

def concat_data01():
    s1=pd.Series([0,1],index=['a','b'])
    s2=pd.Series([2,3,4],index=['c','d','e'])
    s3=pd.Series([5,6],index=['f','g'])
    print pd.concat([s1,s2,s3])
    print pd.concat([s1,s2,s3],axis=1)
    s4=pd.concat([s1*5,s3])
    print pd.concat([s1,s4],axis=1)
    print pd.concat(([s1,s4]),axis=1,join='inner')
    print pd.concat([s1,s4],axis=1,join_axes=[['a','c','b','e']])
    result=pd.concat([s1,s1,s3],keys=['one','two','three'])
    print result
    print result.unstack()
# concat_data01()

def concat_data02():
    df1=DataFrame(np.arange(6).reshape(3,2),index=['a','b','c'],columns=['one','two'])
    df2=DataFrame(5+np.arange(4).reshape(2,2),index=['a','c'],columns=['three','four'])
    print df1
    print df2
    print pd.concat([df1,df2],axis=1,keys=['level1','level2'])
    print pd.concat({'level1':df1,'level2':df2},axis=1)
# concat_data02()

def concat_data03():
    df1=DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
    df2=DataFrame(np.random.randn(2,3),columns=['b','d','a'])
    print pd.concat([df1,df2],axis=0,ignore_index=True)
# concat_data03()

def stack_data01():
    data=DataFrame(np.arange(6).reshape((2,3)),index=pd.Index(['ohio','colorado'],name='state'),columns=pd.Index(['one','two','three'],name='number'))
    print data
    result=data.stack()
    print result
    print result.unstack()
    print result.unstack(0)
    s1=Series([0,1,2,3],index=['a','b','c','d'])
    s2=Series([4,5,6],index=['c','d','e'])
    data2=pd.concat([s1,s2],keys=['one','two'])
    print data2
    print data2.unstack()
    print data2.unstack().stack()
    print data2.unstack().stack(dropna=False)
    df=DataFrame({'left':result,'right':result*5},columns=pd.Index(['left','right'],name='side'))
    print df
    print df.unstack('state')
    print df.unstack('state').stack('side')
# stack_data01()
