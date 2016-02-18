from brian import *
from brian.library.ionic_currents import *

#defaultclock.dt=.01*ms # more precise
El = 10.6 * mV
EK = -12 * mV
ENa = 120 * mV
eqs = MembraneEquation(1 * uF) + leak_current(.3 * msiemens, El)
eqs += K_current_HH(36 * msiemens, EK) + Na_current_HH(120 * msiemens, ENa)
eqs += Current('I:amp')

neuron = NeuronGroup(1, eqs, implicit=True, freeze=True)

trace = StateMonitor(neuron, 'vm', record=True)

run(100 * ms)
neuron.I = 4 * uA
run(100 * ms)
plot(trace.times / ms, trace[0] / mV)
show()