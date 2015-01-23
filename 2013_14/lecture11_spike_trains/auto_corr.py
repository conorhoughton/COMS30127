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

def spiketrain(spike_times,delta_t,t0,t1):
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
    pyplot.savefig("auto_st.pgf")


def barplot(labels,data):
    pyplot.clf()
    fig=pyplot.figure(1,figsize=(5,3))
    pos=arange(len(data))
    pyplot.xticks(pos+0.4,labels)
    pyplot.bar(pos,data,width=0.8)
    pyplot.xlim(0,len(labels))
    pyplot.ylim(0,max(data)+1)
    pyplot.yticks([0,2,4,6,8])
    pyplot.xlabel(u"$\\delta t$ (ms)")
    pyplot.savefig("auto_hist.pgf")

bin_size=1
big_t=20

spike_times=[2,3,8,13,14,18]

delta_t=0.01
t0=0
t1=20

spiketrain(spike_times,delta_t,t0,t1)


t=0

y=[]
time=[]


#pyplot.plot(time,y)
#pyplot.show()


auto_corr=[0]*(2*int((big_t/bin_size))+1)

for t1 in spike_times:
    for t2 in spike_times:
        print t1,t2,int(round((t1-t2+big_t/2.0)/bin_size))
        auto_corr[int(round((t1-t2+big_t/2.0)/bin_size))]+=1

print auto_corr

labels=map(lambda x:bin_size*x-big_t/2.0,range(0,50))
labels=map(lambda x:x if x%2==0 else " ",labels)


barplot(labels[1:20],auto_corr[1:20])

        
