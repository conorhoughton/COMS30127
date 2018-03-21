import matplotlib as mpl
mpl.use('pgf')

pgf_with_pdflatex = {
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": [
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
         ]
}
mpl.rcParams.update(pgf_with_pdflatex)

import random
from math import *
from numpy import arange
import matplotlib.pyplot as pyplot

def spiketrain(spike_times,delta_t,t0,t1,filename):
    fig=pyplot.figure(1,figsize=(5,1))
    t=t0
    values=[]
    times=[]
    spike_times_index=0
    while t<t1:
        times.append(t)
        if spike_times_index<len(spike_times) and t>spike_times[spike_times_index]:
            values.append(1)
            spike_times_index+=1
        else:
            values.append(0)
        t+=delta_t
    pyplot.ylim(0,2)
    pyplot.yticks([])
    pyplot.xlabel(u"$t$ (ms)")
    pyplot.plot(times,values)
    pyplot.savefig(filename)


def barplot(labels,data):
    pyplot.clf()
    fig=pyplot.figure(1,figsize=(5,3))
    pos=arange(len(data))
    pyplot.xticks(pos+0.4,labels)
    pyplot.yticks([0,2,4,6])
    pyplot.bar(pos,data,width=0.8)
    pyplot.xlim(0,len(labels))
    pyplot.ylim(0,max(data)+1)
    pyplot.xlabel(u"$\\delta t$ (ms)")
    pyplot.savefig("cross_hist.pgf")


bin_size=1
big_t=20

#spike_times_1=[3,8,14,18]
#spike_times_2=[4,9,15,17,20]

spike_times_1=[3,9,15,16]
spike_times_2=[5,11,12,17,18,19]


delta_t=0.01
t0=0
t1=20

spiketrain(spike_times_1,delta_t,t0,t1,"cross_st1.pgf")
spiketrain(spike_times_2,delta_t,t0,t1,"cross_st2.pgf")


t=0

y=[]
time=[]


#pyplot.plot(time,y)
#pyplot.show()


auto_corr=[0]*(2*int((big_t/bin_size))+1)

for t1 in spike_times_1:
    for t2 in spike_times_2:
        auto_corr[int((-t1+t2+big_t/2.0)/bin_size)]+=1

print auto_corr[0:50]

labels=map(lambda x:bin_size*x-big_t/2.0,range(0,50))
labels=map(lambda x: x if x%2==0 else " ",labels)

barplot(labels[1:20],auto_corr[1:20])

        

## old version produced random roughly periodic spike trains
## abandoned, needed more artificial examples for simplicity
#delta_t=0.01
#pi=4*atan(1)
#period=10
#rate=0.25
#big_t=20
# while t<big_t:
#     time.append(t)
#     if random.random()<fabs(rate*sin(2*pi*t/period))*delta_t:
#         spike_times.append(t)
#         y.append(1)
#     else:
#         y.append(0)
#     t+=delta_t
