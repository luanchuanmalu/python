# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 12:21:04 2015

@author: Yang
"""

import os
import pandas as pd

#重庆啤酒抄底测试
stock_data = pd.read_csv('D:/Wind/data/MarketDay/600132.SH.MarketDay.csv',parse_dates=[0])
stock_data = stock_data[['MarketTime', 'CLOSE', 'VOLUME']]
stock_data.sort('MarketTime', inplace=True)# 对数据按照【date】交易日期从小到大排序
#取停牌后复牌第一天开始
stock_data = stock_data[(stock_data['MarketTime']>'2011-12-08')]
#stock_data = stock_data[(stock_data['MarketTime']<'2012-05-16')]
stock_data['LOW5_CLOSE'] = pd.rolling_min(stock_data['CLOSE'], 3)
df = pd.DataFrame(stock_data)

s1 = pd.Series(df['CLOSE']>df['LOW5_CLOSE'])
df2=df.copy()
#df2['E'] = s1
df2['新低']=s1
df2['SUM']=pd.Series(pd.rolling_sum(df2['新低'],3))
df2 = df2[(df2['SUM']>2)]
df3=df[df['MarketTime']>df2.iat[0,0]]
print u"开仓日期：",df2.iat[0,0], " 开仓价格:", df2.iat[0,1]
print u"卖出日期：",df3.iat[40,0], " 卖出价格:", df3.iat[40,1]
print u"收益率 %",(df3.iat[40,1]-df2.iat[0,1])/df2.iat[0,1]*100