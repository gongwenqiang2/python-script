#-*- coding: utf-8 -*-
__author__ = 'gongwenqiang'


import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from time import time
from sklearn.neighbors import kneighbors_graph
from sklearn.datasets.samples_generator import make_swiss_roll

n_samples=1500
noise=0.05
X,_=make_swiss_roll(n_samples,noise)
X[:,1] *=.5

print("Compute unstructured hierarchical clustering...")
t0=time()
cluster0=AgglomerativeClustering(n_clusters=6,linkage='ward')
cluster0.fit(X)
elapsed_time=time()-t0
labels=cluster0.labels_
print("Elapsed time: %.2fs" % elapsed_time)
print("Number of points: %i" % labels.size)

fig=plt.figure()
ax=p3.Axes3D(fig)
ax.view_init(7,-80)
for l in np.unique(labels):
    ax.plot3D(X[labels==l,0],X[labels==l,1],X[labels==l,2],'o',color=plt.cm.jet(np.float(l)/ np.max(labels + 1)))
plt.title('Without connectivity constraints (time %.2fs)' % elapsed_time)

print("Compute unstructured hierarchical clustering...")
t0=time()
connectivity=kneighbors_graph(X,n_neighbors=10,include_self=False)
cluster1=AgglomerativeClustering(n_clusters=6,connectivity=connectivity,linkage='ward')
cluster1.fit(X)
elapsed_time=time()-t0
labels=cluster1.labels_
print("Elapsed time: %.2fs" % elapsed_time)
print("Number of points: %i" % labels.size)

fig=plt.figure()
ax=p3.Axes3D(fig)
ax.view_init(7,-80)
for l in np.unique(labels):
    ax.plot3D(X[labels==l,0],X[labels==l,1],X[labels==l,2],'o',color=plt.cm.jet(np.float(l)/ np.max(labels + 1)))
plt.title('With connectivity constraints (time %.2fs)' % elapsed_time)

plt.show()