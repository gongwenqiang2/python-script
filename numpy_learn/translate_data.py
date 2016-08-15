# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import DataFrame,Series

def drop_reqpeat01():
    data=DataFrame({'k1':['one']*3+['two']*4,'k2':[1,1,2,3,3,4,4]})
    print data
    print data.duplicated()
    print data.drop_duplicates()
    data['v1']=range(7)
    print data.drop_duplicates(['k1'])
    print data
    print data.drop_duplicates(['k1','k2'],keep='last')
# drop_reqpeat01()

def add_column01():
    data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                     'corned beef', 'Bacon', 'pastrami', 'honey ham',
                     'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
    print data
    meat_to_animal = { 'bacon': 'pig', 'pulled pork': 'pig','pastrami': 'cow', 'corned beef': 'cow', 'honey ham': 'pig', 'nova lox': 'salmon'}
    print meat_to_animal
    data2=data
    data2['animal']=data['food'].map(str.lower).map(meat_to_animal)
    print data2
    data3=data
    data3['animal']=map(lambda x:meat_to_animal[x.lower()],data3.food)
    print data3
# add_column01()

def replace01():
    data=Series([1,-999.,2.,-999.,-1000.,3.])
    print data
    print data.replace(-999,np.nan)
    print data.replace([-999,-1000],np.nan)
    print data.replace({-999:np.nan,-1000:0})
# replace01()

def change_axis01():
    data = DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
    print data
    print data.index.map(str.upper)
    data.index=data.index.map(str.upper)
    print data
    print data.rename(index=str.title,columns=str.upper)
    print data.rename(index={'OHIO':'INDIANA'},columns={'three':'peekaboo'},inplace=True)
    print data
# change_axis01()

def cut_data():
    ages=[20,22,25,27,21,23,37,31,61,45,41,32]
    bins=[18,25,35,60,100]
    cats=pd.cut(ages,bins)
    print cats
    print cats.levels
    print cats.labels
    print pd.value_counts(cats)
    print pd.cut(ages,[18,25,35,60,100],right=False)
    group_names=['Youth','YoungAdult','MiddleAged','Senior']
    print pd.cut(ages,bins,labels=group_names)
    data=np.random.randn(20)
    print pd.cut(data,4,precision=2)
# cut_data()

def deal_outlier():
    np.random.seed(12345)
    data=DataFrame(np.random.randn(1000,4))
    print data.describe()
    print data[3][np.abs(data[3])>3]
    print data[(np.abs(data)>3).any(1)]
    data[np.abs(data)>3]=np.sign(data)*3
    print data.describe()
# deal_outlier()

def sample01():
    df=DataFrame(np.arange(5*4).reshape(5,4))
    sampler=np.random.permutation(5)
    print sampler
    print df
    print df.take(sampler)
    print df.take(np.random.permutation(len(df))[:3])
# sample01()

def sample02():
    bag=np.array([5,7,-1,6,4])
    sampler=np.random.randint(0,len(bag),size=10)
    print sampler
    draws=bag.take(sampler)
    print draws
# sample02()

def dummy01():
    df=DataFrame({'key':['b','b','a','c','a','b'],'data1':range(6)})
    print df
    print pd.get_dummies(df['key'])
    dummies=pd.get_dummies(df['key'],prefix='key')
    df_with_dummy=df[['data1']].join(dummies)
    print df_with_dummy
# dummy01()

def dummy02():
    mnames=['movies_id','title','genres']
    movies=pd.read_table(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch02\movielens\movies.dat',
                         sep='::',header=None,names=mnames)
    print movies[:10]
    genre_iter=(set(x.split('|')) for x in movies.genres)
    genres=sorted(set.union(*genre_iter))
    print genres
    dummies=DataFrame(np.zeros((len(movies),len(genres))),columns=genres)
    for i,gen in enumerate(movies.genres):
        dummies.ix[i,gen.split('|')]=1
    movies_windic=movies.join(dummies.add_prefix('Genre_'))
    print movies_windic.ix[0]
# dummy02()

def dummy03():
    values=np.random.rand(10)
    print values
    bins=[0,0.2,0.4,0.6,0.8,1]
    print pd.cut(values,bins)
    print pd.get_dummies(pd.cut(values,bins))
dummy03()