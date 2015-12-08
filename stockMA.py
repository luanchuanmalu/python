# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 11:50:01 2015

@author: Yang
"""
import pandas as pd

stock_data=pd.read_csv('D:/Wind/data/000001.SZ.marketDay.csv',parse_dates=[9])
stock_data.sort('TIME', inplace=True)
print stock_data
ma_list = [5, 20, 60]
for ma in ma_list:
    stock_data['MA_' + str(ma)] = pd.rolling_mean(stock_data['CLOSE'], ma)
for ma in ma_list:
    stock_data['EMA_' + str(ma)] = pd.ewma(stock_data['CLOSE'], span=ma)
stock_data.sort('TIME', ascending=False, inplace=True)
stock_data.to_csv('D:/Wind/data/000001_ma_ema.csv', index=False)
