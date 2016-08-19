# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from matplotlib import pyplot as plt

from datetime import datetime,timedelta

def date_12():
    p=pd.Period(2007,freq='A-DEC')
    print p
    print p+5
    print p-2
    print pd.Period('2014',freq='A-DEC')-p

    rng=pd.period_range('1/1/2000','6/30/2000',freq='M')
    print rng
    print Series(np.random.randn(6),index=rng)

    values=['2001Q3','2002Q2','2003Q1']
    index=pd.PeriodIndex(values,freq='Q-DEC')
    print index
# date_12()

def date_13():
    p=pd.Period('2007',freq='A-DEC')
    print p.asfreq('M',how='start')
    print p.asfreq('M',how='end')

    p=pd.Period('2007',freq='A-JUN')
    print p.asfreq('M',how='start')
    print p.asfreq('M',how='end')

    p=pd.Period('2007-08',freq='M')
    print p.asfreq('A-JUN')

    rng=pd.period_range('2006','2009',freq='A-DEC')
    ts=Series(np.random.randn(len(rng)),index=rng)
    print ts
    print ts.asfreq('M',how='start')
    print ts.asfreq('B',how='end')
# date_13()

def date_14():
    rng=pd.date_range('1/1/2000',periods=3,freq='M')
    ts=Series(np.random.randn(3),index=rng)
    pts=ts.to_period()
    print ts
    print pts
    print pts.to_timestamp(how='end')

    rng=pd.date_range('1/29/2000',periods=6,freq='D')
    ts2=Series(np.random.randn(6),index=rng)
    print ts2.to_period('M')
# date_14()

def date_15():
    data=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\macrodata.csv')
    print data.year
    print data.quarter
    index=pd.PeriodIndex(year=data.year,quarter=data.quarter,freq='Q-DEC')
    print index
    data.index=index
    print data.infl
# date_15()

def date_16():
    rng=pd.date_range('1/1/2000',periods=100,freq='D')
    ts=Series(np.random.randn(100),index=rng)
    print ts.resample('M',how='mean')
    print ts.resample('M',how='mean',kind='period')

    rng=pd.date_range('1/1/2000',periods=12,freq='T')
    ts=Series(range(12),index=rng)
    print ts
    print ts.resample('5min',how='sum')
    print ts.resample('5min',how='sum',closed='left',label='left')
    print ts.resample('5min',how='sum',loffset='-1s')

    print ts.resample('5min',how='ohlc')
# date_16()

def date_17():
    rng=pd.date_range('1/1/2000',periods=100,freq='D')
    ts=Series(np.random.randn(100),index=rng)
    print ts.groupby(lambda x:x.month).mean()
    print ts.groupby(lambda x:x.weekday).mean()
# date_17()

def date_18():
    frame = DataFrame(np.random.randn(2, 4),
                      index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                      columns=['Colorado', 'Texas', 'New York', 'Ohio'])
    print frame[:5]
    df_daily=frame.resample('D',fill_method='ffill')
    print df_daily

    print frame.resample('D',fill_method='ffill',limit=2)
# date_18()

def date_19():
    frame=DataFrame(np.random.randn(24,4),
                    index=pd.period_range('1-2000','12-2001',freq='M'),
                    columns=['Colorado', 'Texas', 'New York', 'Ohio'])
    print frame[:5]

    anual_frame=frame.resample('A-DEC',how='mean')
    print anual_frame

    print anual_frame.resample('Q-DEC',fill_method='ffill')
    print anual_frame.resample('Q-DEC',fill_method='ffill',convention='start')
    print anual_frame.resample('Q-MAR',fill_method='ffill')
date_19()