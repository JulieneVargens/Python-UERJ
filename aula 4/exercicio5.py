# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:01:31 2018

@author: Juliene Vargens
"""
#IMC
def imc(massa,altura):
    imc=(massa)/(altura)**2
    return imc
#imc do bebe
print(imc(11,0.7), 'kg/m^2')

#Volume esféra
import math
def volume(raio):
    volume=(4/3)*(math.pi)*(raio**2)
    return volume
print (volume(2),'m^3')

# fendas

def delta_y(lambda1,distancia_anteparo,espacamento_fendas):
    delta_y=((lambda1)*(distancia_anteparo))/(espacamento_fendas)
    return delta_y
print(delta_y(0.0006328,1980,0.250),'mm')

