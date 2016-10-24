#-*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

# License: BSD 3 clause


print __doc__

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time

n_clolors=64
china=load_sample_image('china.jpg')
china=np.array(china,dtype=np.float64)/255

# Load the Summer Palace photo
china = load_sample_image("china.jpg")

# Convert to floats instead of the default 8 bits integer coding. Dividing by
# 255 is important so that plt.imshow behaves works well on float data (need to
# be in the range [0-1])
china = np.array(china, dtype=np.float64) / 255

w,h,d=original_shape=tuple(china.shape)
assert d==3

img_array=np.reshape(china,(w*h,d))

print("Fitting model on a small sub-sample of the data")
t0 = time()
kmeans=KMeans(n_clusters=n_clolors)
img_array_sample=shuffle(img_array,random_state=0)[:1000]
kmeans.fit(img_array)
print "done in %0.3fs." %(time()-t0)

print("Predicting color indices on the full image (k-means)")
t0 = time()
labels=kmeans.predict(img_array)
kmeans_code_book=kmeans.cluster_centers_
print "done in %0.3fs." %(time()-t0)

random_code_book=shuffle(img_array,random_state=0)[:n_clolors+1]
print("Predicting color indices on the full image (random)")
random_labels=pairwise_distances_argmin(random_code_book,img_array,axis=0)
print "done in %0.3fs." %(time()-t0)

def recreate_image(code_book,labels,w,h):
    d=code_book.shape[1]
    new_image=np.zeros((w,h,d))
    label_num=0
    for i in range(w):
        for j in range(h):
            new_image[i,j]=code_book[labels[label_num]]
            label_num +=1
    return new_image

plt.figure(1)
plt.clf()
ax = plt.axes([0, 0, 1, 1])
plt.axis('off')
plt.title('Original image (96,615 colors)')
plt.imshow(china)

plt.figure(2)
plt.clf()
ax=plt.axes([0,0,1,1])
plt.axis('off')
plt.title('Quantized image (64 colors, K-Means)')
plt.imshow(recreate_image(kmeans_code_book,labels,w,h))

plt.figure(3)
plt.clf()
ax=plt.axes([0,0,1,1])
plt.axis('off')
plt.title('Quantized image (64 colors, Random)')
plt.imshow(recreate_image(random_code_book,random_labels,w,h))

plt.show()