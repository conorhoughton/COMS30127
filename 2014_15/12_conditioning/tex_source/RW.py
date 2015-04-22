import numpy as np
import matplotlib.pyplot as plt
from random import randint


epsilon=0.05

ws=[0]
ws_rand=[0]

r=1



for i in range(0,150):
    u=randint(0,1)
    ws.append(ws[-1]+epsilon*(r*u-ws[-1]*u))

r=0

for i in range(0,150):
    u=randint(0,1)
    ws.append(ws[-1]+epsilon*(r-ws[-1]*u))

plt.figure(num=None, figsize=(4, 3), dpi=80, facecolor='w', edgecolor='k')
plt.plot(ws,'yo-')
plt.xlabel('trials')
plt.ylabel("$w$")
#plt.savefig("RW.pgf")
plt.savefig("RW.png")
plt.show()
