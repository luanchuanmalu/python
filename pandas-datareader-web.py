# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 17:46:00 2015

@author: Yang
"""

import pandas.io.data as web
import datetime

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2015,11,3)

f = web.DataReader("000001.SZ",'yahoo',start,end)

print f.ix['2015-10-02']