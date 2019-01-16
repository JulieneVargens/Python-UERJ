# encoding: utf-8

from modulo import ctes,eletron,foton,compton

import random                   # Numeros aleatorios
import matplotlib.pyplot as plt # plots

from math import floor,ceil,pi

XM = pi/6
Xm = pi/30
dt = 1e-3

def plot(x,ys,yl,xl='Ângulo Fóton (rad)',xlim=(Xm,XM)):
    ks = sorted(ys.keys())
    M = -1000
    m = 1000
    for k in ks:
        y = ys[k]
        M = max([M,max(y)])
        m = min([m,min(y)])
        plt.plot(x,y,label=str(k)+'e-16 kg m/s')
    plt.legend(loc='upper right')
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.xlim(xlim[0],xlim[1])
    plt.ylim(1.005*m if m<0 else 0.995*m,1.03*M)
    plt.show()
            
if __name__=="__main__":
    random.seed()
    Efs = dict()                                                        # Energias fóton
    Ees = dict()                                                        # Energias elétrons
    pfs = dict()                                                        # Momentos fótons
    pes = dict()                                                        # Momentos elétrons
    phs = dict()                                                        # Angulos de deflexão do elétron
    for _ in range(5):
        pf0 = tuple([random.uniform(1,10)*1e-14]+[0,0])  # Momento inicial do foton
        key = int(1e16*pf0[0])
        print(pf0)
        f = foton(pf0)                                                  # Fóton com o momento gerado
        e = eletron()                                                   # Elétron
        c = compton(f,e)                                                # Espalhamento
        theta = [i*dt for i in range(int(floor(Xm/dt)),int(ceil(XM/dt)))]         # Vetor de angulos de deflexao do fóton
        Efs[key] = []
        Ees[key] = []
        pfs[key] = []
        pes[key] = []
        phs[key] = []
        for q in theta:                                                 # Para cada theta
            f,e,phi = c.espalha(q)                                      # Faz o espalhamento
            Efs[key].append(f.E())
            Ees[key].append(e.E())
            pfs[key].append(f.P())
            pes[key].append(e.P())
            phs[key].append(phi)

    plot(theta,Efs,'Energia Fóton (J)')
    plot(theta,Ees,'Energia Elétron (J)')
    plot(theta,pfs,'Momento Fóton (kg m/s)')
    plot(theta,pes,'Momento Elétron (kg m/s)')
    plot(theta,phs,'Ângulo Elétron (rad)')
    
