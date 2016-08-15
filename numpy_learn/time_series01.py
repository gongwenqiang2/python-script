# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from matplotlib import pyplot as plt

from datetime import datetime,timedelta
def date_01():
    now=datetime.now()
    print now
    print now.year,now.month,now.day

    delta=datetime(2011,11,7)-datetime(2008,6,28,8,15)
    print delta
    print delta.days
    print delta.seconds

    start=datetime(2011,1,7)
    print start+timedelta(12)
    print start-2*timedelta(12)
# date_01()

def date_02():
    stamp=datetime(2011,1,3)
    print str(stamp)
    print stamp.strftime('%Y-%m-%d')
    value='2011-01-03'
    print datetime.strptime(value,'%Y-%m-%d')

    datestrs=['7/6/2011','8/6/2011']
    print [datetime.strptime(x,'%m/%d/%Y') for x in datestrs]
# date_02()

from dateutil.parser import parse
def date_03():
    print parse('2011-01-03')
    print parse('Jan 31,1991 10:45 PM')
    print parse('6/12/2011',dayfirst=True)

    datestrs=['7/6/2011','8/6/2011']
    print pd.to_datetime(datestrs)
    idx=pd.to_datetime(datestrs+[None])
    print idx
    print pd.isnull(idx)
# date_03()

def date_04():
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
    ts = Series(np.random.randn(6), index=dates)
    print ts
    print type(ts)
    print ts.index

    print ts+ts[::2]
    print ts.index.dtype

    stamp=ts.index[2]
    print stamp
    print ts[stamp]
    print ts['1/10/2011']
    print ts['20110110']


# date_04()

def date_05():
    longer_ts=Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
    print longer_ts
    print longer_ts['2001']
    print longer_ts['2001-05']

    dates=pd.date_range('1/1/2000',periods=100,freq='W-WED')
    long_df=DataFrame(np.random.randn(100,4),
                    index=dates,
                    columns=['Colorado', 'Texas', 'New York', 'Ohio'])
    print long_df.ix['5-2001']
# date_05()

def date_06():
    dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000',  '1/3/2000'])
    dup_ts=Series(np.arange(5),index=dates)
    print dup_ts
    print dup_ts.index.is_unique
    print dup_ts['1/3/2000']
    print dup_ts['1/2/2000']
    grouped=dup_ts.groupby(level=0)
    print grouped.mean()
    print grouped.count()
# date_06()

def date_07():
    dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
    ts = Series(np.random.randn(6), index=dates)
    print ts
    print ts.resample('D')
# date_07()

def date_08():
    index=pd.date_range('4/1/2012','6/1/2012')
    print index

    print pd.date_range(start='4/1/2012',periods=20)
    print pd.date_range(end='6/1/2012',periods=20)

    print pd.date_range('1/1/2000','12/1/2000',freq='BM')

    print pd.date_range('5/2/2012 12:56:31',periods=5)
    print pd.date_range('5/2/2012 12:56:31',periods=5,normalize=True)
# date_08()

def date_09():
    from pandas.tseries.offsets import Hour,Minute
    hour=Hour()
    print hour
    four_hours=Hour(4)
    print four_hours

    print pd.date_range('1/1/2000','3/1/2000 23:59',freq='4h')
    print Hour(2)+Minute(30)
    print pd.date_range('1/1/2000',periods=10,freq='1h30min')

    rng=pd.date_range('1/1/2012','9/1/2012',freq='WOM-3FRI')
    print list(rng)
# date_09()

def date_10():
    ts=Series(np.random.randn(4),index=pd.date_range('1/1/2000',periods=4,freq='M'))
    print ts
    print ts.shift(2)
    print ts.shift(-2)

    print ts/ts.shift(1)-1

    print ts.shift(2,freq='M')
    print ts.shift(3,freq='D')
    print ts.shift(1,freq='3D')
    print ts.shift(1,freq='90T')
# date_10()

def date_11():
    from pandas.tseries.offsets import Day,MonthEnd
    now=datetime(2011,11,17)
    print now+3*Day()
    print now+MonthEnd()
    print now+MonthEnd(2)

    offset=MonthEnd()
    print offset.rollforward(now)
    print offset.rollback(now)

    ts=Series(np.random.randn(20),index=pd.date_range('1/15/2000',periods=20,freq='4d'))
    print ts.groupby(offset.rollforward).mean()
    print ts.resample('M',how='mean')
date_11()