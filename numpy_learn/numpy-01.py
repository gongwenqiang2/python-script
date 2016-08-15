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
# get_ele()

def multi1():
    a=np.arange(0,60,10).reshape(-1,1)+np.arange(0,6)
    print a
    print "数组切片"
    print a[0,3:5]
    print a[4:,4:]
    print a[:2]
    print a[2::2,::2]
<<<<<<< HEAD
    #使用slice()函数创建切片模型
    s=slice(None,None,2),slice(2,None)
    print a[s]
    #s使用numpy内置的s_对象创建切片模型
    print np.s_[::2,2:]
multi1()
=======
# multi()

def struct_array():
    persontype=np.dtype({'names':['name','age','weight'],'formats':['S32','i','f']},align=True)
    a=np.array([("zhang",32,75.5),("wang",24,65.2)],dtype=persontype)
    print a
    print a.dtype
    print a.shape
    print a[0]
    c=a[0]
    c['name']="li"
    print a
    b=a['age']
    print b
    b[0]=40
    print a
# struct_array()

def ufunc_learn():
    x=np.linspace(0,2*np.pi,10)
    print x
    y=np.sin(x)
    print y
    a=np.arange(6.0).reshape(2,3)
    print a.item(1,2) #和a[1,2]类似
    print type(a.item(1,2))
    print type(a[1,2])
# ufunc_learn()

def arithmetic_learn():
    a=np.arange(0,4)
    b=np.arange(1,5)
    print np.add(a,b)
    print np.add(a,b,a)
    print a
    print a+b
# arithmetic_learn()

def compare_learn():
    a=np.array([1,2,3])
    b=np.array([3,2,1])
    print a>=b
    print type(a>b)
    c=np.arange(5)
    d=np.arange(4,-1,-1)
    print c==d
    print c>d
    print np.logical_or(c==d,c>d)
    print np.any(a==b)
# compare_learn()

def broadcast_learn():
    a=np.arange(0,60,10).reshape(-1,1)
    print a
    b=np.arange(0,5)
    print b
    print a+b
broadcast_learn()
>>>>>>> 13b15588afcf4396ee9725fc8155006961a595ed
