
# Authors: Gael Varoquaux, Nelle Varoquaux
# License: BSD 3 clause

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

centers=[[1,1],[-1,-1],[1,-1]]
X,real_clusters=make_blobs(n_samples=750,centers=centers,cluster_std=0.4,random_state=0)
X=StandardScaler().fit_transform(X)

db=DBSCAN(eps=0.3,min_samples=10).fit(X)
core_index=db.core_sample_indices_
is_core=np.zeros(len(X),dtype=bool)
is_core[core_index]=True

labels=db.labels_
n_clusters=len(np.unique(labels))-(1 if -1 in labels else 0)
colors=['b','g','r','c','m','y']
colors=colors[:(n_clusters+1)]
unique_labels=set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for label,color in zip(unique_labels,colors):
    if label==-1:
        color='k'

    class_member_mask = (labels == label)

    xy_core=X[class_member_mask & is_core]
    plt.plot(xy_core[:,0],xy_core[:,1],'o',markerfacecolor=color,markeredgecolor='k',markersize=14)

    xy_other=X[class_member_mask & ~is_core]
    plt.plot(xy_other[:,0],xy_other[:,1],'o',markerfacecolor=color,markeredgecolor='k',markersize=6)


plt.show()