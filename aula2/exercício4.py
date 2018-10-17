# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:11:09 2018

@author: Juliene Vargens
"""

lambda1=0.0006328 #em milimetros
distancia_anteparo= 1980
espacamento_fendas= 0.250
delta_y=((lambda1)*(distancia_anteparo))/(espacamento_fendas)
print(delta_y,'mm')