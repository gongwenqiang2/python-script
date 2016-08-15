# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

def group01():
    df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                    'key2' : ['one', 'two', 'one', 'two', 'one'],
                    'data1' : np.random.randn(5),
                    'data2' : np.random.randn(5)})
    print df
    grouped=df['data1'].groupby(df['key1'])
    print grouped.mean()
    means=df['data1'].groupby([df['key1'],df['key2']]).mean()
    print means
    print means.unstack()
    states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
    years = np.array([2005, 2005, 2006, 2005, 2006])
    print df['data1'].groupby([states,years]).mean()
    print df.groupby('key1').mean()
    print df.groupby(['key1','key2']).mean()
    print df.groupby(['key1','key2']).size()
    for name,group in df.groupby('key1'):
        print name
        print group
    for (k1,k2),group in df.groupby(['key1','key2']):
        print k1,k2
        print group
    pieces=dict(list(df.groupby('key1')))
    print pieces['a']
    print df.dtypes
    grouped=df.groupby(df.dtypes,axis=1)
    print dict(list(grouped))

    print df.groupby(['key1','key2'])['data1'].mean()
    print df.groupby(['key1','key2'])[['data1']].mean()
# group01()

def group02():
    people = DataFrame(np.random.randn(5, 5),
                       columns=['a', 'b', 'c', 'd', 'e'],
                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
    people.ix[2:3,['b','c']]=np.nan
    print people
    mapping= {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f' : 'orange'}
    by_column=people.groupby(mapping,axis=1)
    print by_column.sum()
    map_series=Series(mapping)
    print people.groupby(map_series,axis=1).count()

    print people.groupby(len).sum()
    key_list=['one','one','one','two','two']
    print people.groupby([len,key_list]).min()
# group02()

def group03():
    columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                         [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
    hier_df=DataFrame(np.random.randn(4,5),columns=columns)
    print hier_df

    print hier_df.groupby(level='cty',axis=1).count()
# group03()

def group04():
    df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                    'key2' : ['one', 'two', 'one', 'two', 'one'],
                    'data1' : np.random.randn(5),
                    'data2' : np.random.randn(5)})
    print df
    grouped=df.groupby('key1')
    print grouped['data1'].quantile(0.9)

    def peak_to_peak(arr):
        return arr.max()-arr.min()
    print grouped.agg(peak_to_peak)

    print grouped.describe()
# group04()

def group05():
    tips=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\\tips.csv')
    tips['tip_pct']=tips['tip']/tips['total_bill']
    print tips[:6]
    grouped=tips.groupby(['sex','smoker'])
    grouped_pct=grouped['tip_pct']
    print grouped_pct.agg('mean')

    def peak_to_peak(arr):
        return arr.max()-arr.min()

    print grouped_pct.agg(['mean','std',peak_to_peak])

    print grouped_pct.agg([('foo','mean'),('bar','std')])

    functions=['count','mean','max']
    result=grouped['tip_pct','total_bill'].agg(functions)
    print result
    print result['tip_pct']

    ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
    print grouped['tip_pct','total_bill'].agg(ftuples)

    print grouped.agg({'tip':np.max,'size':'sum'})

    print grouped.agg({'tip_pct':['min','max'],'size':'sum'})
# group05()

def group06():
    people = DataFrame(np.random.randn(5, 5),
                       columns=['a', 'b', 'c', 'd', 'e'],
                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
    key=['one', 'two', 'one', 'two', 'one']
    print people.groupby(key).mean()

    print people.groupby(key).transform('mean')

    def demean(arr):
        return arr-arr.mean()
    demeaned=people.groupby(key).transform(demean)
    print demeaned
    print demeaned.groupby(key).mean()
# group06()

def group07():
    tips=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\\tips.csv')
    tips['tip_pct']=tips['tip']/tips['total_bill']
    def top(df,n=5,column='tip_pct'):
        return df.sort_index(by=column)[-n:]
    print top(tips,n=6)
    print tips.groupby('smoker').apply(top)
    print tips.groupby(['smoker','day']).apply(top,n=1,column='total_bill')
    print tips.groupby('smoker',group_keys=False).apply(top)
# group07()

def group08():
    frame=DataFrame({'data1':np.random.randn(1000),
                     'data2':np.random.randn(1000)})
    factor=pd.cut(frame.data1,4)
    print factor[:10]
    def get_stats(group):
        return {'min':group.min(),'max':group.max(),'count':group.count(),'mean':group.mean()}
    grouped=frame.data2.groupby(factor)
    print grouped.apply(get_stats).unstack()

    grouping=pd.qcut(frame.data1,10,labels=False)
    grouped=frame['data2'].groupby(grouping)
    print grouped.apply(get_stats).unstack()
# group08()

def group09():
    states = ['Ohio', 'New York', 'Vermont', 'Florida',
              'Oregon', 'Nevada', 'California', 'Idaho']
    group_key=['East']*4+['West']*4
    data=Series(np.random.randn(8),index=states)
    data[['Vermont', 'Nevada', 'Idaho']] = np.nan
    print data
    grouped=data.groupby(group_key)
    fill_mean=lambda g:g.fillna(g.mean())
    print grouped.apply(fill_mean)
    print data.fillna(grouped.transform('mean'))

    fill_values={'East':0.5,'West':1}
    fill_value=lambda g:g.fillna(fill_values[g.name])
    print grouped.apply(fill_value)
# group09()

def group10():
    suits=['H','S','C','D']
    cards_val=(range(1,11)+[10]*3)*4
    # print cards_val
    base_names=['A']+range(2,11)+['J','Q','K']
    # print len(base_names)
    cards=[]
    for suit in suits:
        cards.extend(str(num)+suit for num in base_names)
    deck=Series(cards_val,index=cards)
    print deck

    def draw(deck,n=5):
        return deck.take(np.random.permutation(len(deck))[:n])
    print draw(deck)
    get_suit=lambda card:card[-1]

    print deck.groupby(get_suit).apply(draw,n=2)

    print deck.groupby(get_suit,group_keys=False).apply(draw,n=2)
# group10()

def group11():
    df=DataFrame({'category':['a','a','a','a','b','b','b','b'],
                  'data':np.random.randn(8),
                  'weight':np.random.randn(8)})
    print df

    grouped=df.groupby('category')
    get_wavg=lambda g:np.average(g['data'],weights=g['weight'])
    print grouped.apply(get_wavg)
# group11()

def group12():
    close_px=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch09\stock_px.csv',parse_dates=True,index_col=0)
    print close_px[-10:]

    rets=close_px.pct_change().dropna()
    print rets[-10:]
    spx_corr=lambda x:x.corrwith(x['SPX'])
    by_year=rets.groupby(lambda y:y.year)
    print by_year.apply(spx_corr)
    print by_year.apply(lambda x:x['AAPL'].corr(x['SPX']))
# group12()

def group13():
    import statsmodels.api as sm
    def regress(data,yvar,xvar):
        Y=data[yvar]
        X=data[xvar]
        X['intercept']=1
        result=sm.OLS(Y,X).fit()
        return result.params
    close_px=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch09\stock_px.csv',parse_dates=True,index_col=0)
    print close_px[-10:]

    rets=close_px.pct_change().dropna()
    print rets[-10:]
    by_year=rets.groupby(lambda y:y.year)
    print by_year.apply(regress,'AAPL',['SPX'])
# group13()


def group14():
    tips=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch08\\tips.csv')
    tips['tip_pct']=tips['tip']/tips['total_bill']
    print tips.pivot_table(index=['sex','smoker'])
    print tips.pivot_table(['tip_pct','size'],index=['sex','day'],columns='smoker')
    print tips.pivot_table(['tip_pct','size'],index=['sex','day'],columns='smoker',margins=True)
    print tips.pivot_table('tip_pct',index=['sex','smoker'],columns='day',aggfunc=len,margins=True)
    print tips.pivot_table('size',index=['time','sex','smoker'],columns='day',aggfunc='sum',fill_value=0)

    print pd.crosstab([tips['time'],tips['day']],tips.smoker,margins=True)
group14()