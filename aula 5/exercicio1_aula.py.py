# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:29:09 2018

@author: Juliene Vargens
"""
def do_twice (g,x): 
    g(x)
    g(x)
    
def print_spam (x): 
    print(x) 

do_twice (print_spam,'bala')
    
   