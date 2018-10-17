# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:34:37 2018

@author: Juliene Vargens
"""
import time
time_date_hour=time.localtime(time.time())
print(time_date_hour)
time_asc=time.asctime()
print('-------x---------')
print(time_asc)
print('------x-------')
mytuple=(1993,4,6,15,23,15,0,0,0)
print(time.asctime(mytuple))