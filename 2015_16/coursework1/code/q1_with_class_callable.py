import matplotlib.pyplot as plt
import math


#example where the callable is made using a class with a __call__ method
#not needed here but might be useful elsewhere

class Df:

    def __init__(self,n,a,b):
        self.a=a
        self.b=b
        self.n=n
    def __call__(self,f,t):
        return math.pow(f,self.n)-self.a*f+math.exp(self.b*t)

t0=0
t1=3
dt=0.1

f0=0 #not actually defined in the question!

ts=[t0]
fs=[f0]

n=2
a=3.0
b=-1.0

df=Df(n,a,b)

while ts[-1]<t1:
    
    f=fs[-1]+df(fs[-1],ts[-1])*dt
    
    ts.append(ts[-1]+dt)
    fs.append(f)

plt.plot(ts,fs)
plt.xlabel("t (seconds)")
plt.ylabel("f(t)")
plt.title("Euler solution with dt=0.1")


plt.show()

