# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 18:27:00 2015

@author: Yang
"""

import pandas as pd
import numpy as np

s=pd.Series([1,3,5,np.nan,6,8])
print s
dates = pd.date_range('20130101', periods=6)
print dates
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print df2
print df2.dtypes
print df2.C
print df.head()
print df.tail(3)
print df.index
print df.columns
print df.values
print df.describe
print df.T
print df['A']
print df[0:3]
print df['20130102':'20130104']
print df.loc[:,['A','B']]
print df.loc['20130102':'20130104',['A','B']]
print df.loc['20130102',['A','B']]
print df.loc[dates[0],'A']
print df.at[dates[0],'A']
print df.iloc[3]
print df.iloc[[1,2,4],[0,2]]
print df[df.A > 0]
print df[df > 0]
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print df2
print df2[df2['E'].isin(['two','four'])]
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print s1
df['F'] = s1
df.at[dates[0],'A'] = 0
df.iat[0,1] = 0
df.loc[:,'D'] = np.array([5] * len(df))
print df
df2 = df.copy()
df2[df2 > 0] = -df2
print df2
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print df1
print df1.dropna(how='any')
print df1.fillna(value=5)
print df1
print pd.isnull(df1)
print df
print df.mean(1)
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
print s
print df.sub(s, axis='index')
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print s.str.lower()

df = pd.DataFrame(np.random.randn(10, 4))
print df
pieces = [df[:3], df[3:7], df[7:]]
print pd.concat(pieces)
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print pd.merge(left, right, on='key')
print left
print right
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print df
print df.groupby('A').sum()
print df.groupby(['A','B']).sum()
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot()





























