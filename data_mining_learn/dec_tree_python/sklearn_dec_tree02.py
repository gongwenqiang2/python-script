# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import DataFrame,Series
from sklearn import tree,metrics
from sklearn.cross_validation import train_test_split




#导入数据
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



print data['workclass'].value_counts()
#移除“education”列
data=data.drop(u'education',axis=1)

# #首次尝试使用tree生成决策树
#
# #将data拆分为训练集和测试集
# train_features,test_features,train_target,test_target=train_test_split(data.ix[:,:12],data['salarycat'],test_size=0.7,random_state=2)
#
# #创建树对象
# clf=tree.DecisionTreeClassifier(criterion='entropy',min_samples_split=50)
# #通过训练数据集生成决策树
# dec_tree=clf.fit(train_features,train_target)

#使用字符型变量输入决策树创建失败

#对数据集进行规整

#使用pandas提供的applymap函数去除字符型变量的左右空格
data=data.applymap(lambda x:x.strip() if isinstance(x,str) else x)
#将数据集中“？”值制定为缺失值
#将salarycat类编码为0/1类型
data=data.replace({'?':None,'<=50K':-1,'>50K':1})
#通过pandas提供的get_dummies()函数获取哑变量矩阵
data_dummy=pd.get_dummies(data[['workclass','marital-status','occupation','relationship','race','sex','native-country']],
                          prefix=['wkc','mrt','ocp','rls','rc','sex','ntc']).join(data[['age','fnlwgt','education-num','capital-gain','capital-loss','hours-per-week','salarycat']])
#查看哑变量矩阵的列数
print len(data_dummy.columns)
#将data拆分为训练集和测试集
train_f,test_f,train_t,test_t=train_test_split(data_dummy.ix[:,:89],data_dummy['salarycat'],test_size=0.7,random_state=100)

#创建树对象
clf=tree.DecisionTreeClassifier()
#通过训练集创建树模型
dec_tree=clf.fit(train_f,train_t)

#通过测试集生成预测值
pre_t=dec_tree.predict(test_f)
print pre_t

pre_score=metrics.precision_score(test_t,pre_t)
print pre_score

# 第二次创建决策树（不纯度度量指定为熵，最小分支节点样本数指定为50，最小叶节点样本数制定为10）
#创建树对象
clf2=tree.DecisionTreeClassifier(criterion='entropy',min_samples_split=50,min_samples_leaf=10)
#通过训练集创建树模型
dec_tree2=clf2.fit(train_f,train_t)
#通过测试集生成预测值
pre_t2=dec_tree2.predict(test_f)
pre_score=metrics.precision_score(test_t,pre_t2)
print pre_score
