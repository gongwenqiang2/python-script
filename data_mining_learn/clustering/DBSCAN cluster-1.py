#-*- coding: utf-8 -*-

__author__ = 'gongwenqiang'


import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X,labels_true=make_blobs(n_samples=750,centers=centers,cluster_std=0.4,random_state=0)

X=StandardScaler().fit_transform(X)

db=DBSCAN(eps=0.3,min_samples=10).fit(X)
core_sample_mask=np.zeros_like(db.labels_,dtype=bool)
core_sample_mask[db.core_sample_indices_]=True
labels=db.labels_

clusters=len(set(labels))-(1 if -1 in labels else 0)
unique_labels=set(labels)
colors=plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for k,color in zip(unique_labels,colors):
    if k==-1:
        color='k'

    class_member_mask=(labels==k)

    xy=X[class_member_mask & core_sample_mask]
    plt.plot(xy[:,0],xy[:,1],'o',markerfacecolor=color,markeredgecolor='k',markersize=14)

    xy=X[class_member_mask & ~core_sample_mask]
    plt.plot(xy[:,0],xy[:,1],'o',markerfacecolor=color,markeredgecolor='k',markersize=6)

plt.title('Estimated number of clusters: %d' % clusters)
plt.show()