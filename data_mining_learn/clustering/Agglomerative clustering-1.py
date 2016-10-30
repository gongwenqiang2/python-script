#-*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

from time import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph

n_samples=1500
np.random.seed(0)
t = 1.5 * np.pi * (1 + 3 * np.random.rand(1, n_samples))
x = t * np.cos(t)
y = t * np.sin(t)


X = np.concatenate((x, y))
X += .7 * np.random.randn(2, n_samples)
X = X.T

knn_graph=kneighbors_graph(X,30,include_self=False)

for connectivity in (None,knn_graph):
    for n_clusters in (3,30):
        plt.figure(figsize=(10,40))
        for index,linkage in enumerate(('average','complete','ward')):
            plt.subplot(1,3,index+1)
            cluster=AgglomerativeClustering(n_clusters=n_clusters,connectivity=connectivity,linkage=linkage)
            t0=time()
            cluster.fit(X)
            elapsed_time=time()-t0

            plt.scatter(X[:,0],X[:,1],c=cluster.labels_,cmap=plt.cm.spectral)
            plt.title('linkage:%s (time:%.2fs)' %(linkage,elapsed_time),fontdict=dict(verticalalignment='top'))
            plt.axis('equal')
            plt.axis('off')

            plt.subplots_adjust(bottom=0,top=.89,wspace=0,left=0,right=1)
        plt.suptitle('n_clusters=%i,connectivity=%r' %(n_clusters,connectivity is not None),size=17)

plt.show()



