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

def spiketrain(stimulus,spike_times,delta_t,t0,t1):
    fig=pyplot.figure(1,figsize=(5,1))
    t=t0
    values=[]
    times=[]
    spike_times_index=0
    stimulus_index=0
    while t<t1:
        times.append(t)
        if spike_times_index<len(spike_times) and t>spike_times[spike_times_index]:
            values.append(1)
            spike_times_index+=1
        elif stimulus_index<len(stimulus) and t>stimulus[stimulus_index]:
            values.append(2)
            stimulus_index+=1
        else:
            values.append(0)
        t+=delta_t
    pyplot.ylim(0,2)
    pyplot.yticks([])
    pyplot.xlabel(u"$t$ (ms)")
    pyplot.plot(times,values)
    pyplot.savefig("peri_st.pgf")


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
    pyplot.savefig("peri_hist.pgf")

bin_size=1
big_t=55

stimulus=[5,15,25,35,45]

spike_times=[6,6.5,7.5,10,15.5,16.4,17,22,26.9,28,29,35.5,37,38,40.5,41.5,46.5,47.5,48]

delta_t=0.01
t0=0
t1=50

spiketrain(stimulus,spike_times,delta_t,t0,t1)


t=0

y=[]
time=[]


#pyplot.plot(time,y)
#pyplot.show()


auto_corr=[0]*(t1/bin_size+1)

for t1 in stimulus:
    for t2 in spike_times:
        if t2>t1:
            auto_corr[int((t2-t1)/bin_size)]+=1


end_index=(stimulus[1]-stimulus[0])/bin_size

print auto_corr[0:end_index]

labels=map(lambda x:bin_size*x,range(0,end_index))
labels=map(lambda x:x if x%2==0 else " ",labels)

barplot(labels[0:end_index],auto_corr[0:end_index])

        
