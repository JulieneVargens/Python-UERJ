# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:16:17 2018

@author: Juliene Vargens e Marcos Felipe
"""

"""
 Programa que realiza a resolucao de um pendulo com mola e pendulo simples
 utilizando o metodo da soma de Riemman
"""
# Pego da bibiloteca de constantes do scipy o valor da aceleracao da gravidade
from scipy.constants import g
from math import cos, sin, asin, radians, hypot
import matplotlib.pyplot as plt
import numpy as np
# Incremento temporal que serah utilizado
delta_t = 1e-4
# Estes parametros sao associados ao pendulo mola
massa = 2.0
comprimento_natural = 1.0
# Defino a constante elastica no entanto ela pode ser alterada pelo
# usuario durante a execucao do programa (conforme a solicitacao do
# exerci­cio)
constante_elastica = 1.0

# Definicao da aceleracao centripeta que serah usada no calculo da dinamica
# de ambos os pendulos. Esta funcao recebe as velocidades em x e z da massa
# o angulo theta com o eixo z e a distancia da massa ao ponto de fixacao
# do pendulo. Retorna a aceleracao centri­peta em x e em z
def acel_centrip(vx, vz, x, z, r):
   ac = (vx ** 2 + vz ** 2) / r
   ac_x = - ac * x / r
   ac_z = ac * z / r
   return ac_x, ac_z

# Defino a aceleracao do pendulo mola, Dada as entradas das velocidades em theta e r, 
# o angulo theta com o eixo z e a distancia da massa do ponto de fixacao do pendulo
# a funcao retorna as aceleracoes em theta e r
def pend_mola_acel(v_theta, v_r, r, theta):
   a_theta = (-2.0 * v_r * v_theta - g * sin(theta)) / r
   a_r = r * v_theta ** 2 - constante_elastica * (r - comprimento_natural) / massa + g * cos(theta)
   return a_theta, a_r

# Analogamente ao pendulo mola defino a aceleracao do pendulo simples.
def pend_simples_acel(v_theta, v_r, r, theta) :
   a_theta = - g/r * sin(theta)
   a_r = 0.0
   return a_theta, a_r
   
# Uma vez que todos os dados que o usuario informara sao do tipo ponto flutuante
# a funcao recebe os dados e o retorna convertidos.
def pegar_os_dados_float(mensagem_da_tela = ""):
   return float(input(mensagem_da_tela))

# Definicao de como sera dado o passo no metodo de integracao.
def passo_de_riemman(f, df, dt):
   return f + df * dt

def escrever_dados(saida, tempo, x, z, vel_x, vel_z, r, mod_v, mod_acel, E):
   saida.write("%f %f %f %f %f %f %f %f %f \n" %(tempo, x, z, vel_x, vel_z, r, mod_v, mod_acel, E))

# Como o sistema possui apenas forcas conservativas a energia permanece constante.
# As variacoes que podem ser vistas no grafico E vs t eh apenas imprecisao
# do metodo utilizado.
def energia(l0, r, theta, mod_v) :
   E_cinetico = massa * (mod_v ** 2) * 0.5
   E_pot_grav = - massa * g * r *cos(theta)
   E_pot_elastica = constante_elastica * ((r - l0) ** 2) * 0.5
   return E_cinetico + E_pot_grav + E_pot_elastica

# Funcao que realizarah a integracao. Recebe o tempo inicial, tempo final, deslocamento
# angular, deslocamento radial da massa, velocidade em r e theta e aceleracao inicial.
# Escreve os dados em cada passo de tempo n na saida especificada.
def soma_de_riemman(saida, tempo_ini, tempo_max, theta_graus, r, v_theta, v_r, acel, l0):
# Defino as condicoes iniciais das variaveis
   theta = radians(theta_graus)
   x = r * sin(theta)
   z = -r * cos(theta)
   v_tan = r * v_theta
   mod_v = hypot(v_tan, v_r)
   a_theta, a_r = acel(v_theta, v_r, r, theta)
   a_tan = r * a_theta
   mod_a = hypot(a_tan, a_r)
   vx = mod_v * sin(theta)
   vz = -mod_v * cos(theta)
   tempo = tempo_ini
   E = energia(l0, r, theta, mod_v)
   n = 0

   while tempo <= tempo_max:
      escrever_dados(saida, tempo, x, z, vx, vz, r, mod_v, mod_a, E)
      v_theta = passo_de_riemman(v_theta, a_theta, delta_t)
      v_r = passo_de_riemman(v_r, a_r, delta_t)
      v_tan = r * v_theta
      mod_v = hypot(v_tan, v_r)
      vx = mod_v * sin(theta)
      vz = -mod_v * cos(theta)
      r = passo_de_riemman(r, v_r, delta_t)
      theta = passo_de_riemman(theta, v_theta, delta_t)
      x = r * sin(theta)
      z = - r * cos(theta)
      a_theta, a_r = acel(v_theta, v_r, r, theta)
      a_tan = r * a_theta
      mod_a = hypot(a_tan, a_r)
      tempo = tempo_ini + n * delta_t
      E = energia(l0, r, theta, mod_v)
      n += 1
# Funcao que dado o nome do arquivo, o ti­tulo e o formato, plota os graficos solicitados
# no projeto.
def plotar_graficos(nome_arquivo, title, formato):
   print("Plotando os graficos de " + title)
   z_vs_x = np.loadtxt(nome_arquivo, usecols = (1, 2))
   v_vs_t = np.loadtxt(nome_arquivo, usecols = (0, 6))
   r_vs_t = np.loadtxt(nome_arquivo, usecols = (0, 5))
   a_vs_t = np.loadtxt(nome_arquivo, usecols = (0, 7))
   vx_vs_x = np.loadtxt(nome_arquivo, usecols = (1, 3))
   vz_vs_z = np.loadtxt(nome_arquivo, usecols = (2, 4))
   E_vs_t = np.loadtxt(nome_arquivo, usecols = (0, 8))
   graficos = [z_vs_x, v_vs_t, r_vs_t, a_vs_t, vx_vs_x, vz_vs_z, E_vs_t]
   xlabels = ["x", "t", "t", "t", "x", "z", "t"]
   ylabels = ["z", "V", "r", "a", "Vx", "Vz", "E"]
   for i in range(len(graficos)):
      plt.figure(i)
      plt.xlabel(xlabels[i])
      plt.ylabel(ylabels[i])
      plt.title(title)
      plt.plot(graficos[i][:,0], graficos[i][:,1])
      nome_fig = nome_arquivo[:-4] + "_"+ ylabels[i] + "_vs_" + xlabels[i] + "." + formato
      plt.savefig(nome_fig)
   plt.close('all')

def pendulo_simples():
   print("PENDULO SIMPLES")
   print()
   print("Para o calculo do pendulo simples por favor informe os seguintes dados:")
   comprimento_haste = pegar_os_dados_float("comprimento da haste: ")
# Pego o angulo inicial em graus pois fica mais facil para o usuario pensar em graus
# do que em multiplos de pi no caso de radianos.
   theta_0_graus = pegar_os_dados_float("deslocamento angular inicial (em graus): ")
   tempo_max = pegar_os_dados_float("tempo maximo considerado no calculo (em segundos): ")
# Crio um nome de arquivo para cada execucao do programa com diferentes parametros
   nome_arquivo = ("Pendulo_simples_l=%f_theta0=%f_tmax=%f.txt" %(comprimento_haste, theta_0_graus, tempo_max))

# Estas condicoes iniciais nao estao definidas dentro da funcao de integracao para que 
# as condicoes iniciais do pendulo simples fiquem independentes da do pendulo mola
# durante a execucao do programa.
   tempo_inicial = 0.0
   vel_theta = 0.0
   vel_r = 0.0

# Preparo o arquivo de saida dos dados:
   saida = open(nome_arquivo, 'w')
   soma_de_riemman(saida, tempo_inicial, tempo_max, theta_0_graus, comprimento_haste, vel_theta, vel_r, pend_simples_acel, comprimento_haste)
   saida.close()
   
   print()
   print("Calculos completados com sucesso.")
   print("Os dados foram salvos em " + nome_arquivo)
   print()
   plotar_graficos(nome_arquivo, "Pendulo Simples", "png")   
   
def pendulo_mola():
   print("PENDULO MOLA")
   print()
   print("O pendulo mola esta configurado com comprimento natural comprimento_natural = %f e massa = %f"
         %(comprimento_natural, massa))
   print("Para o calculo por favor informe os seguintes dados:")
   constante_elastica = pegar_os_dados_float("Constante elastica da mola (em N/m): ")
# Pego o comprimento da mola no instante inicial pois fica mais facil para o usuario
# pensar no comprimento total da mola do que a posicao exata x,z da massa.
   r = pegar_os_dados_float("Comprimento da mola neste instante t0: ")
# Pego o angulo inicial em graus pois fica mais facil para o usuario pensar em graus
# do que em multiplos de pi no caso de radianos.
   theta_0_graus = pegar_os_dados_float("deslocamento angular inicial (em graus): ")
   tempo_max = pegar_os_dados_float("tempo maximo considerado no calculo (em segundos): ")
   nome_arquivo = ("Pendulo_mola_l0=%f_k=%f_r=%f_theta0=%f_tmax=%f.txt" %(comprimento_natural, 
                                         constante_elastica ,r, theta_0_graus, tempo_max))

# Estas condicoes iniciais nao estao definidas dentro da funcao de integracao para que 
# as condicoes iniciais do pendulo simples fiquem independentes da do pendulo mola
# durante a execucao do programa.
   tempo_inicial = 0.0
   vel_r = 0.0
   vel_theta = 0.0
   
   saida = open(nome_arquivo, 'w')
   soma_de_riemman(saida, tempo_inicial, tempo_max, theta_0_graus, r, vel_theta, vel_r, pend_mola_acel, comprimento_natural)
   saida.close()
   
   print()
   print("Calculos completados com sucesso.")
   print("Os dados foram salvos em " + nome_arquivo )
   print()
   plotar_graficos(nome_arquivo, "Pendulo Mola", "png")
   
pendulo_simples()
pendulo_mola()
