import matplotlib.pyplot as plt
import math

def df(f,t):
    return math.pow(f,2)-3*f+math.exp(-t)

t0=0
t1=3
dt=0.1

f0=0 #not actually defined in the question!

ts=[t0]
fs=[f0]

while ts[-1]<t1:
    
    f=fs[-1]+df(fs[-1],ts[-1])*dt
    
    ts.append(ts[-1]+dt)
    fs.append(f)

plt.plot(ts,fs)
plt.xlabel("t (seconds)")
plt.ylabel("f(t)")
plt.title("Euler solution with dt=0.1")


plt.show()

