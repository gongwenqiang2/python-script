# -*- coding: utf-8 -*-

import numpy as np
#hh
def numpy_array01():
    a=np.array([1,2,3,4])
    print a
    print a.shape
    b=np.array((5,6,7,8))
    print b
    print b.shape
    c=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print c
    print c.shape
    d=np.array([[1],[2],[3],[4]])
    print d
    print d.shape
    c.shape=(4,3)
    print c
    c.shape=(2,-1)
    print c
    d=a.reshape(2,2)
    print d
    #d和a共享储存空间，修改a的数值d也会随之改变，修改d的数值a也会随之改变
    a[1]=100
    d[0,0]=100
    print d
    print a
    print "--数组的dtype属性"
    print c.dtype
    print np.array([1,2,3,4],dtype=float)
    print np.array([1,2,3,4],dtype=complex)
    print "完整的数据类型列表"
    print set(np.typeDict.values())
# numpy_array01()

def numpy_createarray():
    print "arrange()函数"
    a=np.arange(0,1,0.1)
    print a
    print "linspace函数"
    print np.linspace(0,1,10)
    print np.linspace(0,1,10,endpoint=False)
    print "logspace()函数生成等比数列"
    print np.logspace(0,2,10)
    print np.logspace(0,1,12,False,base=2) #指定底数为2
    print "zeros()函数创建数组"
    print np.zeros((2,3),dtype=int)
    print "ones()函数"
    print np.ones((2,3),dtype=np.float)
    print "empty()函数（不对内数值初始化)"
    print np.empty((2,3),dtype=np.int)
    print "使用frombuffer()函数从字节序列创建数组"
    print np.frombuffer("abcdefg",dtype=np.int8)
# numpy_createarray()

def use_fromfunction():
    def func(i):
        return i/4+1
    a=np.fromfunction(func,(10,))
    print a
    # 创建9*9乘法表
    def func2(i,j):
         return (i+1)*(j+1)
    b=np.fromfunction(func2,(9,9))
    print b
# use_fromfunction()

def get_ele():
    x=np.arange(10,1,-1)
    print x
    print x[[1,2]]
    b=x[np.array([3,3,1,8])]
    print b
    c=x[np.array([[3,3,1,8],[3,3,-1,8]])]
    print c
    d=x[[1,5,8,6,4,7,1,6]]
    print d.reshape(2,-1)
get_ele()
