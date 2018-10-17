#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:27:17 2018

@author: howardhsu
"""

# JTC 20181011

from datetime import date
import calendar
from sys import argv

#today = datetime.now().weekday()
#print(today)

print("YYYYMMDD", end=' ')
x = input()

y = datetime.strptime(x, "%Y%m%d").weekday()

weekday = calendar.day_name[y]

print(f"It's %s on %s" %(weekday, x))