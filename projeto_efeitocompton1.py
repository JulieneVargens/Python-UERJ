# encoding: utf-8
# Python3

from math import sqrt,pi,sin,cos,tan,atan

def cotan(x):
    return 1.0/tan(x)

class ctes:                             # Classe de constantes físicas
    c = 299792458                       # Velocidade da luz em m/s    
    me = 9.109e-31                      # Massa do elétron em kg
    e = 1.6e-19                         # Carga do elétron

class v4:                               # Classe para o quadrivetor
    def __init__(self,t=0,x=0,y=0,z=0): # Construtor da classe
        self.v=(t,x,y,z)                # 4-vetor
        
    def __str__(self):                  # Cast para string
        return '('+';'.join([str(a) for a in self.v])+')'
        
    def __add__(self,other):            # Sobrecarga do operador +
        return v4(self.v[0]+other.v[0],self.v[1]+other.v[1],self.v[2]+other.v[2],self.v[3]+other.v[3])
        
    def __sub__(self,other):            # Sobrecarga do operador -
        return v4(self.v[0]-other.v[0],self.v[1]-other.v[1],self.v[2]-other.v[2],self.v[3]-other.v[3])
        
    def __mul__(self,other):            # Sobrecarga do operador *
        if type(other)==float:
            x = other
            return v4(self.v[0]*x,self.v[1]*x,self.v[2]*x,self.v[3]*x)
        return sum([a*b for a,b in zip(self.v,other.v)])
        
    def __truediv__(self,x):            # Sobrecarga do operador *
        return v4(self.v[0]/x,self.v[1]/x,self.v[2]/x,self.v[3]/x)
    
    def __getitem__(self,key):          # Sobrecarga do operador []
        return self.v[key]
        
class particula:                        # Classe que representa uma partícula
    def __init__(self,m=0,p=v4()):      # Construtor
        self.m0 = m                     # Massa de repouso da partícula
        self.p = p                      # Momento 4-vetor da partícula
    
    def E(self):                        # Energia
        return sqrt(self.P()**2*ctes.c**2+self.m0**2*ctes.c**4)
        
    def P(self):                        # Momento linear
        return sqrt(self.p[1]**2+self.p[2]**2+self.p[3]**2)
        
class eletron(particula):               # Eletron
    def __init__(self,p=v4()):
        super().__init__(ctes.me,p)     # Particula com a massa do eletron
        
class foton(particula):                 # Fóton
    def __init__(self,p=v4()):
        if type(p)==tuple:
            p = v4(sqrt(p[0]**2+p[1]**2+p[2]**2),p[0],p[1],p[2])
        super().__init__(p=v4(sqrt(p[1]**2+p[2]**2+p[3]**2),p[1],p[2],p[3]))
        
    def E(self):                        # Energia do fóton
        return self.p[0]*ctes.c
    
class compton:
    def __init__(self,f,e):                                 # Inicializa a classe do espalhamento
        self.f = f                                          # Fóton
        self.e = e                                          # Elétron
        
    def phi_e(self,theta):                                  # Angulo de deflexão do elétron
        if theta==0:
            return 0
        return atan(cotan(0.5*theta)/(1+self.f.E()/self.e.E()))
        
    def momento4(self,theta,phi,Ef,Ee):                     # Quadrivetores momentum
        if theta==0:
            return self.f.p,self.e.p
        pf = self.f.P()/(cos(theta)+cotan(phi)*sin(theta))  # Momento do fóton (módulo)
        pe = self.e.P()/(cos(phi)+cotan(theta)*sin(phi))    # Momento do elétron (módulo)
        pf = v4(Ef/ctes.c,pf*cos(theta),pf*sin(theta),0)    # Quadrimomento do fóton
        pe = v4(Ee/ctes.c,pe*cos(phi),pe*sin(phi),0)        # Quadrimomento do elétron
        return pf,pe
        
    def energia(self,theta):
        Ef = 1.0/(1.0/self.f.E()+(1.0-cos(theta))/self.e.E())# Energia do fóton
        Ee = self.f.E()+self.e.E()-Ef                       # Energia do elétron
        return Ef,Ee
        
    def espalha(self,theta):                                # Faz o espalhamento
        Ef1,Ee1 = self.energia(theta)                       # Energias finais
        phi = self.phi_e(theta)                             # Angulo de deflexão do elétron
        pf1,pe1 = self.momento4(theta,phi,Ef1,Ee1)          # Momentos finais
        return foton(pf1),eletron(pe1),phi
