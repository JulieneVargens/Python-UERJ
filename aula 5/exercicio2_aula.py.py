# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:54:40 2018

@author: Juliene Vargens
"""
def do_twice (f,x): 
    f(x)
    f(x)

def do_four (f,x): 
       do_twice (f,x)
       do_twice (f,x)

def print_spam (x): 
    print(x) 

do_four(print_spam,'bala')
