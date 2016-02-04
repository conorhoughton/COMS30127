from math import *


class Leaky:
    
    def __init__(self,tau,delta_t,v_0):
        self.v=v_0
        self.tau=tau
        self.delta_t=delta_t

    def update(self,input):
        self.v=(self.v-input)*exp(-self.delta_t/self.tau)+input
        return self.v


delta_t= 0.1
tau1=0.25
tau2=2
tau3=4

leaky1=Leaky(tau1,delta_t,0)
leaky2=Leaky(tau2,delta_t,0)
leaky3=Leaky(tau3,delta_t,0)

t=0
big_t=20

while t<big_t:
    input=sin(t)
    v1=leaky1.update(input)
    v2=leaky2.update(input)
    v3=leaky3.update(input)
    print t,v1,v2,v3,input
    t+=delta_t

