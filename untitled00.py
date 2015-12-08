# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:18:00 2015

@author: Yang
"""
import pandas as pd
df = pd.read_csv("D:/Wind/data/f.csv")

from pivottablejs import pivot_ui

pivot_ui(df)