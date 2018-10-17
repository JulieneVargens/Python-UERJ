# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:43:19 2018

@author: Juliene Vargens
"""
'Atividade 1'
#
ts= 30          #tempo em segundos
tm=43           #tempo em minutos
tc=tm*60        #passando de minuto para segundo
t=ts+tc
d=10            #Distância em quilômetros
dm=10/(1.61)    #Passando de quilômetros para milhas
H=t/dm
print(H,'s/mi')
th=t/60         #Passando o tempo total para horas
v=dm/th
print(v,'mi/h')