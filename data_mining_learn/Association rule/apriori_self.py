#-*- coding: utf-8 -*-
__author__ = 'gongwenqiang'


import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import itertools

def get_data():
    data=pd.read_csv('http://spaces.ac.cn/usr/uploads/2015/07/3424358296.txt', header=None, dtype = object)
    return data

def dummy_data(data):
    dummy=pd.get_dummies(data,prefix='',prefix_sep='')
    return dummy

def get_sup(d_data,lk):
    lk_data=d_data[lk]
    if isinstance(lk,list):
        l=len(lk)
    else:
        l=1
        return (lk_data==l).sum()
    sup_lk=(lk_data.sum(axis=1)==l).sum()
    return sup_lk

def aprior(b_lk,k):
    aprior_l=[]
    l=len(b_lk)
    for i in range(l-2):
        lk_head_1=b_lk[i][:k-2]
        for j in range(i+1,l-1):
            l0=b_lk[i][:]
            lk_head_2=b_lk[j][:k-2]
            lk_tail_1=b_lk[i][k-2]
            lk_tail_2=b_lk[j][k-2]
            if lk_head_1==lk_head_2 and lk_tail_1<>lk_tail_2:
                l0.append(b_lk[j][k-2])
                aprior_l.append(l0)
    return aprior_l

# aprior([['A2'],['B1'],['B2'], ['C1'], ['C2'], ['D1'], ['D2'], ['E1'], ['E2'], ['H4']],k=2)

def get_lk(d_data,min_sup):
    len_d=len(d_data)
    lk_sup_0=DataFrame([get_sup(d_data,i) for i in d_data.columns],index=d_data.columns,columns=['sup'])
    lk_sup=lk_sup_0[lk_sup_0>=len_d*min_sup].dropna()
    b_lk=sorted([[x] for x in lk_sup.index])
    k=1
    while(len(b_lk)>1):
        k=k+1
        aprior_k=aprior(b_lk,k)
        lk_sup_0=DataFrame([get_sup(d_data,i) for i in aprior_k],index=['-'.join(x) for x in aprior_k],columns=['sup'])
        lk_sup_1=lk_sup_0[lk_sup_0>=len_d*min_sup].dropna()
        lk_sup=pd.concat([lk_sup,lk_sup_1])
        b_lk_0=sorted([x for x in lk_sup_1.index])
        b_lk=[x.split('-') for x in b_lk_0]
    lk_sup=dict(zip(lk_sup.index,lk_sup.sup))
    return lk_sup

def get_conf(lk_sup,lk,fore_lk):
    confidence=lk_sup[lk]/lk_sup[fore_lk]
    return confidence

def get_fandq_lk(lk):
    lk=lk.split('-')
    fore_lk=[]
    conseq_lk=[]
    for i in range(len(lk)-1):
        i=i+1
        f0=list(itertools.combinations(lk,i))
        fore_lk.extend(['-'.join(x) for x in f0])
        for x in f0:
            lk1=lk[:]
            for y in x:
                lk1.remove(y)
            conseq_lk.append('-'.join(lk1))
    return fore_lk,conseq_lk

# print get_fandq_lk( 'C1-D1-E2')

def get_rule(lk_sup,min_conf):
    rule={}
    for lk in lk_sup.keys():
        fore_lk,conseq_lk=get_fandq_lk(lk)
        l=len(fore_lk)
        lk0=lk.split('-')
        for i in range(l):
            item=fore_lk[i]
            conf=get_conf(lk_sup,lk,item)
            if conf>=min_conf:
                rule_name= item+'-->'+conseq_lk[i]
                rule[rule_name]=[lk_sup[lk],conf]
    return rule

def aprior_main(data,min_sup,min_conf):
    d_data=dummy_data(data)
    lk_sup=get_lk(d_data,min_sup)
    return get_rule(lk_sup,min_conf)

data=get_data()
print aprior_main(data,0.05,0.7)



