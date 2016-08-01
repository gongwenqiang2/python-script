# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import sys
import csv
import json
import sqlite3

def file_rw01():
    names=['a','b','c','d','message']
    print pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch06\ex2.csv',names=names,index_col='message')
    result=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch06\ex6.csv')
    print result
    print pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch06\ex6.csv',nrows=5)
    chunker=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch06\ex6.csv',chunksize=1000)
    print chunker
# file_rw01()

def file_rw02():
    data=pd.read_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch06\ex5.csv')
    print data
    data.to_csv(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch06\out.csv')
    print '----------'
    data.to_csv(sys.stdout,sep='|')
    print '----------'
    data.to_csv(sys.stdout,na_rep='NULL')
    print '----------'
    data.to_csv(sys.stdout,index=False,header=False)
    print '----------'
    data.to_csv(sys.stdout,index=False,cols=['a','b','c'])
# file_rw02()

def file_rw03():
    f=open(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch06\ex7.csv')
    print f
    reader=csv.reader(f)
    for line in reader:
        print line
# file_rw03()

def file_rw04():
    con=sqlite3.connect(':memory:')
    query="""create table test(a varchar(20),b varchar(20),c real,d INTEGER );"""
    def inserttable():
        con.execute(query)
        con.commit()
    inserttable()
    data=[('Atlanta', 'Georgia', 1.25, 6),
            ('Tallahassee', 'Florida', 2.6, 3),
            ('Sacramento', 'California', 1.7, 5)]
    stmt="insert into test values(?,?,?,?)"
    def insertdata():
        con.executemany(stmt,data)
        con.commit()
    insertdata()
    cursor=con.execute('select * from test')
    rows=cursor.fetchall()
    print rows
    print cursor.description
    print DataFrame(rows,columns=zip(*cursor.description)[0])
    import pandas.io.sql as sql
    sframe=sql.read_sql('select * from test',con)
    print sframe
file_rw04()

