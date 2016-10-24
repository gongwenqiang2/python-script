# -*- coding: utf-8 -*-

__author__ = 'gongwenqiang'

import numpy as np
import math
import random
import matplotlib.pyplot as plt


def get_distance(vector1,vector2):
    distance=math.sqrt(pow(vector1-vector2,2).sum())
    return distance


def initCentroids(dataset,k):
    numSamples,dim=dataset.shape
    centroids=dataset[random.sample(range(numSamples),k)]
    return centroids

def calCentroid(dataset):
    n=len(dataset)
    centroid=sum(dataset)/n
    return centroid

def kmeans(dataset,k):
    centroids=initCentroids(dataset,k)
    cluster=np.zeros(len(dataset))
    print "初始化中心点为："
    print centroids
    clusterChanged=True
    n=0
    while clusterChanged:
        n +=1
        print "开始第 %d 次迭代" %n
        cluster0=cluster.copy()
        for i in range(len(dataset)):
            minDistance=pow(10,10)
            for j in range(k):
                distance=get_distance(dataset[i],centroids[j])
                if distance<minDistance:
                    minDistance=distance
                    cluster[i]=j
        for j in range(k):
            dataset_k=dataset[cluster==j]
            centroids[j]=calCentroid(dataset_k)
        if (cluster0==cluster).all():
            clusterChanged=False
        print "第 %d 次迭代完成的中心点为：" %n
        print centroids
    return cluster,centroids



file=open('testSet.txt','r')
dataSet=[]
for line in file.readlines():
    lineArr=line.strip().split('\t')
    dataSet.append([float(lineArr[0]),float(lineArr[1])])
dataSet=np.array(dataSet)

cluster,centroids=kmeans(dataSet,4)

mark=['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
n=len(dataSet)
k=len(centroids)
for i in range(n):
    plt.plot(dataSet[i, 0], dataSet[i, 1], mark[int(cluster[i])])
for j in  range(k):
    plt.plot(centroids[j, 0], centroids[j, 1], mark[j],markersize = 12)

plt.show()