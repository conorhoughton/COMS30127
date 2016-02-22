
import matplotlib.pyplot as plt
import math

def d_f(f,t):
    return math.pow(f,2)-3.0*f+math.exp(-t)

t0=0
t1=3

dt=0.01


t=t0+dt

#no initial condition was given in the question, using f(0)=0
ts=[t0]
fs=[0]

while t<=t1:
    f=fs[-1]+d_f(fs[-1],ts[-1])*dt
    ts.append(t)
    fs.append(f)
    t+=dt

plt.plot(ts,fs)
plt.show()
