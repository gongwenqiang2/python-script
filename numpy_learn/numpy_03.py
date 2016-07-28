# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np

def np_save():
    arr=np.arange(10)
    np.save("some_array",arr)
# np_save()

def np_load():
    arr=np.load('some_array.npy')
    print arr
# np_load()

def np_savez():
    arr=np.arange(10)
    np.savez('array_archive',a=arr,b=arr-1)
    arch=np.load('array_archive.npz')
    print arch['a']
    print arch['b']
# np_savez()

def np_dot():
    x=np.arange(1,7).reshape(2,-1)
    print x
    y=np.arange(1,7).reshape(3,-1)
    print y
    print x.dot(y)
    print np.dot(x,y)
    print np.dot(x,np.ones(3))
# np_dot()

def np_linalg():
    from numpy.linalg import inv,qr
    x=np.random.randn(5,5)
    mat=x.T.dot(x)
    print mat
    print inv(mat)
    print mat.dot(inv(mat))
    q,r=r(mat)
    print r
# np_linalg()

def np_random():
    samples=np.random.normal(size=(4,4))
    print samples
np_random()