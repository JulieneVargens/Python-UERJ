# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:37:50 2018

@author: Juliene Vargens
"""

def v(xi,x,ti,t):
    v=(x-xi)/(t-ti)
    return v

print(v(5,10,1,2)) #teste

g=10
def ve(vo,to,te):
    ve=vo+(g*(te-to))
    return ve

print(ve(1,1,3)) #teste
    

