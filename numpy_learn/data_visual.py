# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from pandas import DataFrame,Series
import pandas as pd
import mpl_toolkits.basemap

def matpl01():
    fig=plt.figure()
    ax1=fig.add_subplot(2,2,1)
    ax2=fig.add_subplot(2,2,2)
    ax3=fig.add_subplot(2,2,3)
    plt.plot(np.random.randn(50).cumsum(),'k--')
    _=ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
    ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
    # fig.show();sleep(5)
    fig,axes=plt.subplots(2,3)
    print axes
# print matpl01()

def matplt02():
    fig,axes=plt.subplots(2,2,sharex=True,sharey=True)
    for i in range(2):
        for j in range(2):
            axes[i,j].hist(np.random.randn(500),bins=50,color='k',alpha=0.5)
    plt.subplots_adjust(wspace=0,hspace=0)
    plt.show()
# matplt02()

def matplt03():
    plt.plot(np.random.randn(30).cumsum(),color='k',linestyle='dashed',marker='o')
    plt.show()
# matplt03()

def matplt04():
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(np.random.randn(1000).cumsum())
    ticks=ax.set_xticks([0,250,500,750,1000])
    labels=ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')
    ax.set_title('My first matplotlib plot')
    ax.set_xlabel('Stages')
    plt.show()
# matplt04()


def matplot05():
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(np.random.randn(1000).cumsum(),'k',label='one')
    ax.plot(np.random.randn(1000).cumsum(),'k--',label='two')
    ax.plot(np.random.randn(1000).cumsum(),'k.',label='three')
    ax.legend(loc='best')
    plt.show()
# matplot05()

def matplot06():
    from datetime import datetime
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    data=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\spx.csv',index_col=0,parse_dates=True)
    spx=data['SPX']
    print spx[:10]
    spx.plot(ax=ax,style='k-')
    # plt.show()
    crisis_data = [(datetime(2007, 10, 11), 'Peak of bull market'),
                   (datetime(2008, 3, 12), 'Bear Stearns Fails'),
                   (datetime(2008, 9, 15), 'Lehman Bankruptcy')]
    for date,label in crisis_data:
        ax.annotate(label,xy=(date,spx.asof(date)+50),xytext=(date,spx.asof(date)+200),arrowprops=dict(facecolor='black'),
                    horizontalalignment='left',verticalalignment='top')
    ax.set_xlim(['1/1/2007','1/1/2011'])
    ax.set_ylim([600,1800])
    ax.set_title('Important dates in 2008-2009 financial crisis')
    plt.show()
# matplot06()

def matplot07():
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    rect=plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)
    circ=plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)
    pgon=plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color='g',alpha=0.3)

    ax.add_patch(rect)
    ax.add_patch(circ)
    ax.add_patch(pgon)

    plt.show()
# matplot07()

def pdplot01():
    s=Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
    s.plot()
    plt.show()
# pdplot01()

def pdplot02():
    df=DataFrame(np.random.randn(10,4).cumsum(0),
                 columns=['A','B','C','D'],
                 index=np.arange(0,100,10))
    df.plot()
    plt.show()
# pdplot02()

def pdplot03():
    fig,axes=plt.subplots(2,1)
    data=Series(np.random.randn(16),index=list('ABCDEFGHIJKLMNOP'))
    data.plot(kind='bar',ax=axes[0],color='k',alpha=0.7)
    data.plot(kind='barh',ax=axes[1],color='k',alpha=0.7)
    plt.show()
# pdplot03()

def pdplot04():
    df=DataFrame(np.abs(np.random.randn(6,4)),index=['one','two','three','four','five','six'],
                 columns=pd.Index(['A','B','C','D'],name='GENUS'))
    print df
    df.plot(kind='bar')
    plt.show()
    df.plot(kind='barh',stacked=True,alpha=0.5)
    plt.show()
    df_pcts=df.div(df.sum(1).astype(float),axis=0)
    print df_pcts
    df_pcts.plot(kind='bar',stacked=True)
    plt.show()
# pdplot04()

def pdplot05():
    tips=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\\tips.csv')
    print tips[:5]
    party_counts=pd.crosstab(tips.day,tips['size'])
    print party_counts
    party_counts=party_counts.ix[:,2:5]
    party_pct=party_counts.div(party_counts.sum(1).astype(float),axis=0)
    party_pct.plot(kind='bar',stacked=True)
    plt.show()

    tips['tip_pct']=tips['tip']/tips['total_bill']
    tips['tip_pct'].hist(bins=50)
    plt.show()
    tips['tip_pct'].plot(kind='kde')
    plt.show()
# pdplot05()

def pdplot06():
    comp1=np.random.normal(0,1,size=200)
    comp2=np.random.normal(10,2,size=200)
    values=Series(np.concatenate([comp1,comp2]))
    values.hist(bins=100,alpha=0.3,color='k',normed=True)
    values.plot(kind='kde',style='k--')
    plt.show()
# pdplot06()

def pdplot07():
    macro=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\macrodata.csv')
    data=macro[['cpi','m1','tbilrate','unemp']]
    trans_data=np.log(data).diff().dropna()
    print trans_data[-5:]
    plt.scatter(trans_data['m1'],trans_data['unemp'])
    plt.title('Changes in log %s vs. log %s' %('m1','unemp'))
    plt.show()
    pd.scatter_matrix(trans_data,diagonal='kde',color='k',alpha=0.3)
    plt.show()
# pdplot07()


def haiti_map():
    data=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\haiti.csv')
    print data[['INCIDENT DATE','LATITUDE','LONGITUDE']][:10]
    print data['CATEGORY'][:6]
    print data.describe()
    data=data[(data.LATITUDE>18)&(data.LATITUDE<20)&(data.LONGITUDE>-75)&(data.LONGITUDE<-70)&(data.CATEGORY.notnull())]

    def to_cat_list(catstr):
        stripped=(x.strip() for x in catstr.split(','))
        return [x for x in stripped if x]
    def get_all_categories(cat_series):
        cat_sets=(set(to_cat_list(x)) for x in cat_series)
        return sorted(set.union(*cat_sets))
    def get_english(cat):
        codes,names=cat.split('.')
        if '|' in names:
            names=names.split('|')[1]
        return codes,names.strip()
    print get_english('1. Urgences | Emergency')
    print to_cat_list('1. Urgences | Emergency, 3. Public Health,')

    all_cats=get_all_categories(data.CATEGORY)
    english_mapping=dict(get_english(x) for x in all_cats)
    print english_mapping['2a']

    def get_codes(seq):
        return [x.split('.')[0] for x in seq if x]
    all_codes=get_codes(all_cats)
    # print all_codes[:10]
    code_index=pd.Index(np.unique(all_codes))
    dummy_frame=DataFrame(np.zeros((len(data),len(code_index))),index=data.index,columns=code_index,)
    # print dummy_frame.ix[:,:5]

    for row,cat in zip(data.index,data.CATEGORY):
        codes=get_codes(to_cat_list(cat))
        dummy_frame.ix[row,codes]=1
    data=data.join(dummy_frame.add_prefix('category_'))
    print data.ix[:5,10:15]

    from mpl_toolkits.basemap import Basemap

    def basic_haiti_map(ax=None,lllat=17.25,urlat=20.25,lllon=-75,urlon=-71):
        m=Basemap(ax=ax,projection='stere',
                lon_0=(urlon+lllon)/2,
                lat_0=(urlat+lllat)/2,
                llcrnrlat=lllat,urcrnrlat=urlat,
                llcrnrlon=lllon,urcrnrlon=urlon,
                resolution='f')
        m.drawcoastlines()
        m.drawstates()
        m.drawcountries()
        return m

    fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(12,10))
    fig.subplots_adjust(hspace=0.05,wspace=0.05)
    to_plot=['2a','1','3c','7a']
    lllat=17.25;urlat=20.25;lllon=-75;urlon=-71
    for code,ax in zip(to_plot,axes.flat):
        m=basic_haiti_map(ax,lllat=lllat,urlat=urlat,lllon=lllon,urlon=urlon)
        cat_data=data[data['category_%s' %code]==1]
        # print cat_data[['LONGITUDE','LATITUDE']]
        x,y=m(cat_data.LONGITUDE.values,cat_data.LATITUDE.values)
        m.plot(x,y,'k.',alpha=0.5)
        ax.set_title('%s:%s' %(code,english_mapping[code]))
    plt.show()
haiti_map()