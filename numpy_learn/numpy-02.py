# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np

def sub_obj():
    a=np.arange(3*4*5).reshape(3,4,5)
    lidx=[[0],[1],[2]]
    print a[lidx]
    adix=np.array(lidx)
    print adix
    print a[adix]
# sub_obj()

def funcs01():
    a=np.random.randint(0,10,size=(4,5))
    print a
    print sum(a)
    print np.sum(a)
    print np.sum(a,axis=0)
    print np.sum(a,axis=1)
    print np.mean(a)
    print np.mean(a,axis=1)
# funcs01()

def suoyin():
    arr3d=np.arange(1,13).reshape(2,2,3)
    print arr3d
    arr3d0=arr3d[0]
    print arr3d0
    old_values=arr3d0.copy()
    arr3d[0]=42
    print arr3d
    arr3d[0]=old_values
    print arr3d
# suoyin()

def bull_slice():
    names=np.array(["bob","joe","will","bob","will","joe","joe"])
    data=np.random.randn(7,4)
    print data
    print names=="bob"
    print data[names=="bob"]
    print data[names=="bob",2]
    mask=(names=="bob")|(names=="will")
    print mask
    mask2=(names=="bob")&(names!="will")
    data[data<0]=0
    print data
# bull_slice()

def np_where():
    xarr=np.arange(0,5)
    yarr=np.arange(6,11)
    cond=np.array([True,False,True,True,False])
    print xarr
    print yarr
    result1=[(x if c else y ) for x,c,y in zip(xarr,cond,yarr)]
    print result1
    result2=np.where(cond,xarr,yarr)
    print result2
    arr=np.random.randn(4,4)
    print arr
    print np.where(arr>0,2,-2)
    print np.where(arr>0,2,arr)
    arr=np.random.randn(100)
    print (arr>0).sum()
# np_where()

def np_sort():
    arr=np.random.randn(8)
    print arr
    arr.sort()
    print arr
    arr1=np.random.randn(5,3)
    print arr1
    arr1.sort(1)
    print arr1
# np_sort()

def np_unique():
    names=np.array(["bob","joe","will","bob","will","joe","joe"])
    print np.unique(names)
    values=np.arange(1,7)
    print values
    print np.in1d(values,[2,3,6])
np_unique()