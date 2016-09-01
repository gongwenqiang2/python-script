# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from sklearn import tree,metrics
from sklearn.cross_validation import train_test_split


#导入和规整数据
#导入adult数据集
data=pd.read_csv(u'D:\study\数据分析\实验数据集\数据挖掘数据集\\adultdata.csv',sep=',')
print data.tail(5)
#对数据集最后一列列名命名为“salarycat”
data.columns=[u'age', u'workclass', u'fnlwgt', u'education', u'education-num',
       u'marital-status', u'occupation', u'relationship', u'race', u'sex',
       u'capital-gain', u'capital-loss', u'hours-per-week', u'native-country',
       u'salarycat']
print data.columns
#查看属性分布
print data['salarycat'].value_counts()
#将数据集中“？”值制定为缺失值
data.replace({'?':None})
print data['workclass'].value_counts()
#移除“education”列
data=data.drop(u'education',axis=1)

#将data拆分为训练集和测试集
train_features,test_features,train_target,test_target=train_test_split(data.ix[:,13],data['salarycat'],test_size=0.7,random_state=2)

#创建树对象
clf=tree.DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
#通过训练数据集生成决策树
dec_tree=clf.fit(train_features,train_target)