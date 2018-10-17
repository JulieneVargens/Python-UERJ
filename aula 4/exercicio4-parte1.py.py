# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:06:46 2018

@author: Juliene Vargens
"""

def c(milha):
    c=milha*1609.34
    return c
print(c(1)) #teste

def co(metro):          #conversão de metros para milhas
    co=(metro)/(1609.34)
    return co
print(co(1)) #teste
    
def segundo(hora):     #conversão de hora para segundos
    segundo=hora*3600
    return segundo
print(segundo(2)) #test

def hora(segundo):
    hora=segundo/3600
    return hora
print(hora(1))  #teste

def segun(minuto):
    segun=minuto*60
    return segun
print(segun(1))  #teste

def timeinhours(minute):
    timeinhours=minute/60
    return timeinhours

def quilometro(mile):
    quilometro=mile*1.60934
    return quilometro
    
print(quilometro(4),'t')


#exercicio 1-aula 1 revisitado
tempo=43.5      #minutos
distancia=10000
tempo_medio=(segun(43.5))/(co(10000))
print(tempo_medio,'segundos/milhas')

#velocidade media
tempo_segundos=segun(43.5)
tempo_horas=hora(tempo_segundos)
v=distancia/tempo_horas
print(v,'milhas/horas')

# ultima parte do exercicio
temp=30  #minutos
dist=4 #milhas
temp_horas= timeinhours(temp)
dist_quilometro= quilometro(4)
velocidade=dist_quilometro/temp_horas
print(velocidade,'km/h')
