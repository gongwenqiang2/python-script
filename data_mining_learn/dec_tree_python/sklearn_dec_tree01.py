# -*- coding: utf-8 -*-

#导入依赖库
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
#导入树类
from sklearn import tree,metrics
#导入数据训练集拆分方法
from sklearn.cross_validation import train_test_split
#导入鸢尾花数据对象
from sklearn.datasets import load_iris


#创建决策树对象
clf=tree.DecisionTreeClassifier(criterion='entropy',min_samples_split=10)
print clf

#导入鸢尾花数据
data=load_iris()
print data.keys()

#为便于观察将鸢尾花数据集转化为Dataframe格式
data_df=DataFrame(data['data'],columns=data['feature_names'])
species_dict=dict(zip([0,1,2],data['target_names']))
data_df['species']=map(lambda x:species_dict[x],data['target'])
print data_df.head()


#创建训练和测试数据集
train_feartures,test_features,train_classfies,test_classfies=train_test_split(data['data'],data['target'],test_size=0.75,random_state=2)
#通过训练数据集生成决策树
dec_tree=clf.fit(train_feartures,train_classfies)

#对测试集属性进行预测分类
pre_classfies=dec_tree.predict(test_features)
print pre_classfies[:5]
#计算分类准确率
pre_score=metrics.precision_score(test_classfies,pre_classfies)
print pre_score
#测试集属性进行预测分类及概率
pre_proba=dec_tree.predict_proba(test_features)
print pre_proba[:5]

#将决策树导出为Graphviz 格式（可用word打开）
import os
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(dec_tree, out_file=f)
#可使用os的ulink()函数删除该文件
# os.unlink("iris.dot")

#绘制决策树图形导出为pdf格式
from sklearn.externals.six import StringIO
import pydot


dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,feature_names=data['feature_names'],class_names=data['target_names'])
print dot_data.getvalue()
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")


print dir(pydot)