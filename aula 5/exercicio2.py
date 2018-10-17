# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:15:33 2018

@author: Juliene Vargens
"""
def fat(n):
    for i in range(n-1,1,-1):n*=i
    return n

def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1) 
    