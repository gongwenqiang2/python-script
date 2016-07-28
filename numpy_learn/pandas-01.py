# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'


from pandas import DataFrame,Series
import pandas as pd
import numpy as np

def pd_series():
    obj=Series([4,7,-5,3])
    print obj
    print obj.index
    print obj.values
    obj2=Series([4,7,-5,3],index=['d','b','a','c'])
    print obj2
    print obj2.index
    print obj2['a']
    print obj2[obj2>0]
    print 'a' in obj2
# pd_series()

def pd_series2():
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3=Series(sdata)
    print obj3
    stats=['California', 'Ohio', 'Oregon', 'Texas']
    obj4=Series(sdata,index=stats)
    print obj4
    print pd.isnull(obj4)
    print pd.notnull(obj4)
    print obj3+obj4
    obj4.name='population'
    obj4.index.name='state'
    print obj4
# pd_series2()

def pd_dataframe():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame=DataFrame(data)
    print frame
    print DataFrame(data,columns=['year','state','pop'])
    frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four', 'five'])
    print frame2
    print frame2['state']
    print frame2.year
    print frame2.ix['three']
    frame2.debt=16.5
    print frame2
    frame2['debt']=np.arange(5.)
    print frame2
    val=Series(data=[-1.2,-1.5,-1.7],index=['two','four','five'])
    frame2['debt']=val
    print frame2
    frame2['eastern']=frame2.state=='Ohio'
    print frame2
    del frame2['eastern']
    print frame2.columns
# pd_dataframe()

def pd_dataframe2():
    pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
    frame3=DataFrame(pop)
    print frame3
    print frame3.T
    frame4=DataFrame(pop,index=[2001,2002,2003])
    print frame4
    frame3.index.name='year'
    frame3.columns.name='state'
    print frame3
    print frame3.values
# pd_dataframe2()

def pd_dataframe3():
    obj=Series(range(3),index=['a','b','c'])
    print obj
    index= obj.index
    print index
    print index[1:]
    index[1]='d'#不能随意更改索引值
# pd_dataframe3()

def pd_dataframe4():
    obj=Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
    print obj
    obj2=obj.reindex(['a','b','c','d'])
    print obj2
    obj2=obj.reindex(['a','b','c','d','e'])
    print obj2
    obj2=obj.reindex(['a','b','c','d','e'],fill_value=0)
    print obj2
    obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
    obj4=obj3.reindex(range(6),method='ffill')
    print obj4
    obj4=obj3.reindex(range(6),method='bfill')
    print obj4
# pd_dataframe4()

def pd_dataframe5():
    frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],columns=['Ohio', 'Texas', 'California'])
    print frame
    frame2=frame.reindex(['a','b','c','d'])
    print frame2
    stats=['Texas','Utah','California']
    print frame.reindex(columns=stats)
    frame=frame.reindex(index=['a','b','c','d'],method='ffill',columns=stats)
    print frame
    print frame.ix[['a','b','c','d'],stats]
# pd_dataframe5()

def pd_dataframe6():
    obj=DataFrame(np.arange(5.),index=['a','b','c','d','e'])
    print obj
    new_obj=obj.drop('c')
    print new_obj
    print obj.drop(['b','c'])
    data = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])
    print data
    print data.drop(['Ohio', 'Colorado'])
    print data.drop('two',axis=1)
    print data.drop(['two','four'],axis=1)
pd_dataframe6()