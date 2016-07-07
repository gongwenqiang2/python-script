# -*- coding: utf-8 -*-

import numpy as np

def numpy_shape01():
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

numpy_shape01()