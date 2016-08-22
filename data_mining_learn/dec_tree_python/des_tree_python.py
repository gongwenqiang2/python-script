# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import math




#name columns
columns=['sepal_length','sepal_width','petal_length','petal_width','species']
# get data
try:
    data=DataFrame(pd.read_csv(u'D:\git\python-script\data_mining_learn\knn_learn_python\iris.data.csv',header=None))
except:
    data=DataFrame(pd.read_csv(u'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None))
data.columns=columns


#get sample and test data
def split_dataset(dataset,bin):
    sampler=np.random.permutation(len(dataset))
    random_data=dataset.reindex(sampler)
    train_data=random_data[:int(len(dataset)*bin)]
    test_data=random_data[int(len(dataset)*bin):]
    return train_data,test_data




#entropy calculate function
def calc_entropy(s):
    s_len=len(s)
    label_counts=s.value_counts()
    label_p=label_counts/s_len
    # print label_p
    entropy=-sum(map(lambda x:x*(math.log(x,2)),label_p.values))
    return entropy

# entropy=calc_entropy(train_data.species)
# print entropy


def get_node(dataset,attribute,limit_child_num=1):
    entropy_list=[]
    entropy_list[:]=[]
    for feature in dataset.columns[dataset.columns != attribute]:
        data_ranked=dataset.sort_values([feature,attribute])
        d_len=len(data_ranked)
        for x in range(d_len-1):
            if x>limit_child_num-1 and x<d_len-limit_child_num:
                a1,f1=data_ranked.iloc[x][[attribute,feature]]
                a2,f2=data_ranked.iloc[x+1][[attribute,feature]]
                if a1 != a2:
                    s1=data_ranked[data_ranked[feature]<=f1][attribute]
                    s2=data_ranked[data_ranked[feature]>f1][attribute]
                    p1=(x+1)/float(d_len)
                    p2=1-p1
                    entropy_list.append((feature,(f1+f2)/2,p1*calc_entropy(s1)+p2*calc_entropy(s2)))
    node_point=sorted(entropy_list,key=lambda x:x[2])[0][:2]
    leaf1=dataset[dataset[node_point[0]]<=node_point[1]]
    leaf2=dataset[dataset[node_point[0]]>node_point[1]]
    return node_point,leaf1,leaf2


def stop_cond(s,limit_parent_num=20,limit_p=0.9):
    s_len=len(s)
    label_counts=s.value_counts()
    label_p=label_counts/s_len
    if s_len<limit_parent_num or label_p.max()>limit_p:
        return "y",label_counts.index[-1]
    else:
        return "n",None


def create_tree(dataset,attribute='species',limit_parent_num=20,limit_child_num=1,limit_p=0.9):
    df_tree=DataFrame(columns=['code_id','parent_code_id','direct','feature','point','attribute'])
    code_id=[-1]
    feature=[0]
    point=[0]
    def recur_tree(leaf,parent_code_id=-1,direct=0):
        code_id[0]=code_id[0]+1
        is_stop,attr=stop_cond(leaf[attribute],limit_parent_num,limit_p)
        if is_stop=='y':
            df_tree.loc[code_id[0]]=[code_id[0],parent_code_id,direct,None,0,attr]
            return None
        else:
            node_point,leaf1,leaf2=get_node(leaf,attribute,limit_child_num=limit_child_num)
            feature[0]=node_point[0]
            point[0]=node_point[1]

            df_tree.loc[code_id[0]]=[code_id[0],parent_code_id,direct,feature[0],point[0],None]
            parent_code_id=code_id[0]
            recur_tree(leaf1,parent_code_id,'left')
            recur_tree(leaf2,parent_code_id,'right')
    recur_tree(dataset)
    return df_tree



def tree_rule(s,df_tree,parent_code_id=-1,direct=0,attribute=None):
    if not attribute is None:
        return attribute
    else:
        tree_code=df_tree[(df_tree['parent_code_id']==parent_code_id)&(df_tree['direct']==direct)].iloc[0]

        parent_code_id=tree_code['code_id']

        feature=tree_code['feature']
        if not feature is None:
            if s[feature]<=tree_code['point']:
                direct='left'
            else:
                direct='right'

        attribute=tree_code['attribute']

        return tree_rule(s,df_tree,parent_code_id,direct,attribute)



def pre_data(data,df_tree):
    data['pre_attribute']=[tree_rule(data.loc[i],df_tree) for i in data.index]
    return data


train_data,test_data=split_dataset(dataset=data,bin=0.7)
# print train_data

df_tree=create_tree(train_data,'species',5,1,0.95)
print df_tree

test_pre=pre_data(test_data,df_tree)

print len(test_pre[test_pre['species']==test_pre['pre_attribute']])/float(len(test_pre))

