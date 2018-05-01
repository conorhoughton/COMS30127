from math import *


class asy:
    
    def __init__(va,vb):
        self.va=va
        self.vb=vb

    def __call__(v):
        return 0.5*(1+tanh((v-self.va)/self.vb))

class tau:
    
    def __init__(va,vb,phi):
        self.va=va
        self.vb=vb
        self.phi=phi

    def __call__(v):
        return 1/(self.phi*cosh((v-self.va)/self.vb))



mv=0.001
ms=0.001

el=-60*mv
gca=2
eca=120*mv
gk=4
ek=-84*mv
v1=-1.2*mv
v2=18*mv
v3=2*mv
v4=30*mv
phi=0.04


    
