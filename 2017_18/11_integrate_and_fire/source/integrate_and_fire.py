#simple program used to make the integrate and fire figure 

from math import *

e_l = -70
tau_m = 10
v_t = -55
v_spike = 20

r_i = 12

delta_t = 0.1

t=0

big_t=100

v=e_l

while t<=big_t:
	v=(v-e_l-r_i)*exp(-delta_t/tau_m)+e_l+r_i
	if v>=v_t:
            v=e_l
            print t,v_spike	
	else:
            print t,v

	t+=delta_t


