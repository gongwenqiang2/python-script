# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from matplotlib import pyplot as plt

def date_20():
    close_px_all=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch09\stock_px.csv',parse_dates=True,index_col=0)
    close_px=close_px_all[['AAPL','MSFT','XOM']]
    # print close_px[:5]
    close_px=close_px.resample('B',fill_method='ffill')
    print close_px[:5]
    close_px['AAPL'].plot()
    plt.show()

    close_px.ix['2009'].plot()
    plt.show()

    close_px['AAPL'].ix['01-2011':'03-2011'].plot()
    plt.show()

    appl_q=close_px['AAPL'].resample('Q-DEC',fill_method='ffill')
    appl_q.ix['2009':].plot()
    plt.show()
# date_20()

def date_21():
    close_px_all=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch09\stock_px.csv',parse_dates=True,index_col=0)
    close_px=close_px_all[['AAPL','MSFT','XOM']]

    close_px['AAPL'].plot()
    pd.rolling_mean(close_px.AAPL,250).plot()
    plt.show()

    appl_std250=pd.rolling_std(close_px.AAPL,250,min_periods=10)
    print appl_std250[5:12]
    appl_std250.plot()
    plt.show()

    pd.rolling_mean(close_px,60).plot(logy=True)
    plt.show()
# date_21()

def date_22():
    close_px_all=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch09\stock_px.csv',parse_dates=True,index_col=0)
    close_px=close_px_all[['AAPL','MSFT','XOM']]

    fig,axes=plt.subplots(2,1,sharex=True,sharey=True,figsize=(12,7))
    aapl_px=close_px.AAPL['2005':'2009']

    ma60=pd.rolling_mean(aapl_px,60,min_periods=50)
    ewmao60=pd.ewma(aapl_px,span=60)

    aapl_px.plot(style='k-',ax=axes[0])
    ma60.plot(style='k--',ax=axes[0])

    aapl_px.plot(style='k-',ax=axes[1])
    ewmao60.plot(style='k--',ax=axes[1])

    axes[0].set_title('Simple MA')
    axes[1].set_title('Exponentially-Weighted MA')

    plt.show()
date_22()
