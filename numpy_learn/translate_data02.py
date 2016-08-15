# -*- coding: utf-8 -*-
__author__ = 'gongwenqiang'

import numpy as np
import pandas as pd
from pandas import DataFrame,Series

def deal_string01():
    val='a,b, guido'
    print val.split(',')
    pieces=[x.strip() for x in val.split(',')]
    print pieces
    print '::'.join(pieces)
    print 'guido' in val
    print val.index(',')
    # print val.index(':')
    print val.find(':')
    print val.count(',')
    print val.replace(',','::')
    print val.replace(',','')
# deal_string01()

def deal_string02():
    import json
    db=json.load(open(u'D:\study\书籍\python\pydata-book-master\pydata-book-master\ch07\\foods-2011-10-03.json'))
    print len(db)
    print db[0]
    print db[0].keys()
    print db[0]['nutrients'][0]
    nutrients=DataFrame(db[0]['nutrients'])
    print nutrients[:7]
    info_keys=['description','group','id','manufacturer']
    info=DataFrame(db,columns=info_keys)
    print info[:5]
    print pd.value_counts(info.group)[:10]

    nutrients=[]
    for rec in db:
        fnuts=DataFrame(rec['nutrients'])
        fnuts['id']=rec['id']
        nutrients.append(fnuts)
    nutrients=pd.concat(nutrients,ignore_index=True)
    print nutrients
    print nutrients.duplicated().sum()
    nutrients=nutrients.drop_duplicates()
    col_mapping={'description':'food','group':'fgroup'}
    info=info.rename(columns=col_mapping,copy=False)
    print info
    col_mapping={'description':'nutrient','group':'nutgroup'}
    nutrients=nutrients.rename(columns=col_mapping,copy=False)
    print nutrients
    ndata=pd.merge(nutrients,info,on='id',how='outer')
    print ndata
    print ndata.ix[3000]
    result=ndata.groupby(['nutrient','fgroup'])['value'].quantile(0.5)
    # print result
    result['Zinc, Zn'].sort_values().plot(kind='barh')
    by_nutrient=ndata.groupby(['nutgroup','nutrient'])
    get_maximum=lambda x:x.xs(x.value.idxmax())
    get_minimum=lambda x:x.xs(x.value.idmin())
    max_foods=by_nutrient.apply(get_maximum)[['value','food']]
    max_foods.food=max_foods.food.str[:50]
    print max_foods.ix['Amino Acids']['food']
deal_string02()