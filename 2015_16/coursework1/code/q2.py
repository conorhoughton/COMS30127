import matplotlib.pyplot as plt
import math


def df(f,t):
    return math.pow(f,2)-3*f+math.exp(-t)

def euler(df,t0,t1,dt,f0):
    
    ts=[t0]
    fs=[f0]

    while ts[-1]<t1:
    
        f=fs[-1]+df(fs[-1],ts[-1])*dt
    
        ts.append(ts[-1]+dt)
        fs.append(f)
        
    return ts,fs

t0=0
t1=3
f0=0.0

dts=[0.01,0.1,0.5,1]

for dt in dts:
    ts,fs=euler(df,t0,t1,dt,f0)
    plt.plot(ts,fs,label=str(dt))
    plt.legend(loc=2)

plt.xlabel("t (seconds)")
plt.ylabel("f(t)")
plt.title("Euler solution with different dt")


plt.show()

