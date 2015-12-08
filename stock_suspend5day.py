# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 12:01:31 2015

@author: Yang
"""

import os
import pandas as pd

# ========== 遍历数据文件夹中所有股票文件的文件名，得到股票代码列表stock_code_list
stock_code_list = []
for root, dirs, files in os.walk('D:/Wind/data/MarketDay'):# 注意：这里请填写数据文件在您电脑中的路径
    if files:
        for f in files:
            if '.csv' in f:
                stock_code_list.append(f.split('.csv')[0])

print u"统计5日停牌抄底策略"
# ========== 根据上一步得到的代码列表，遍历所有股票，将这些股票合并到一张表格all_stock中
all_stock = pd.DataFrame()
resultfilepath='D:/Wind/data/stock_suspend5days.csv'
all_stockfile=open(resultfilepath,"w")
all_stockfile.write("stockid")
all_stockfile.write(",buydate")
all_stockfile.write(",buyclose")
all_stockfile.write(",selldate")
all_stockfile.write(",sellclose")
all_stockfile.write(",rate%")
# 遍历每个创业板的股票
for code in stock_code_list:
    print code    
    # 从csv文件中读取该股票数据
    stock_data = pd.read_csv('D:/Wind/data/MarketDay/' + code + '.csv',parse_dates=[0])# 注意：这里请填写数据文件在您电脑中的路径
    stock_data = stock_data[['MarketTime', 'CLOSE', 'VOLUME', 'StockId']]
    stock_data.sort('MarketTime', inplace=True)# 对数据按照【date】交易日期从小到大排序
    # 计算5天成交量平均为0,则为停牌5天股票，
    stock_data = stock_data[(stock_data['MarketTime']>'2005-01-01')]
    stock_data = stock_data[(stock_data['MarketTime']<'2015-07-16')]
    stock_data['SUM6_VOLUME'] = pd.rolling_sum(stock_data['VOLUME'], 6)
    #过滤数据 停牌第五天 复牌位置
    stock_data_df=pd.DataFrame(stock_data)
    s1 = pd.Series(stock_data_df['SUM6_VOLUME']==stock_data_df['VOLUME'])
    stock_data_df[u"复牌位置"]=s1
    stock_data_df = stock_data_df[stock_data_df['VOLUME']>0]
    stock_data_df = stock_data_df[stock_data_df[u'复牌位置']==True]
    #使用抄底策略 计算每个复牌位置 买点 收益率 6 7 8 9 10
    #stock_data_df["开仓日期"]=stock_data_df['MarketTime']
    #stock_data_df["开仓价格"]=stock_data_df['CLOSE']
    #stock_data_df["卖出日期："]=stock_data_df['MarketTime']
    #stock_data_df["卖出价格"]=stock_data_df['CLOSE']
    #stock_data_df["收益率"]=stock_data_df['CLOSE']
    sdate=stock_data_df['MarketTime']
    all_stockfile.write("\n")
    for date in sdate:
        #print date
        try:
            stock_data = stock_data[(stock_data['MarketTime']>date)]
            stock_data['LOW5_CLOSE'] = pd.rolling_min(stock_data['CLOSE'], 3)
            t_df = pd.DataFrame(stock_data)
            ts1 = pd.Series(t_df['CLOSE']>t_df['LOW5_CLOSE'])
            t_df2=t_df.copy()
            t_df2['新低']=ts1
            t_df2['SUM']=pd.Series(pd.rolling_sum(t_df2['新低'],3))
            t_df2 = t_df2[(t_df2['SUM']>2)]
            t_df3=t_df[t_df['MarketTime']>t_df2.iat[0,0]]
            #all_stockfile.write("股票代码")
            all_stockfile.write(t_df2.iat[0,3])
            all_stockfile.write(", ")
            #all_stockfile.write(",开仓日期")
            all_stockfile.write(t_df2.iat[0,0])
            all_stockfile.write(", ")
            #all_stockfile.write(",开仓价格")
            all_stockfile.write(str(t_df2.iat[0,1]))
            all_stockfile.write(", ")
            #all_stockfile.write(",卖出日期")
            all_stockfile.write(t_df3.iat[40,0])
            all_stockfile.write(", ")
            #all_stockfile.write(",开仓日期")
            all_stockfile.write(str(t_df3.iat[40,1]))
            all_stockfile.write(", ")
            #all_stockfile.write(",收益率%")
            all_stockfile.write(str((t_df3.iat[40,1]-t_df2.iat[0,1])/t_df2.iat[0,1]*100))
            all_stockfile.write("\n")
        except Exception as err:
            all_stockfile.write("\n")
            print ""

    #输出数据  
    #filepath='D:/Wind/data/5-2/'+ code + '5-1.csv'
    #print u"输出:%s:" %filepath
    #stock_data_df.to_csv(filepath, index=False)
    #print u"停牌位置:%s:" %stock_data['MarketTime']

    

print u"统计结束"
