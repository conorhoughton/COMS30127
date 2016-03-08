e_l=-70
tau_m = 10
v_t = -55

r_i =10

delta_t = 0.1

t=0

big_t=300

v=e_l

while t<=big_t:
	v+=(e_l-v+r_i)*delta_t/tau_m
	if v>v_t:
		v=e_l
		print t,0
	else:
		print t,v

	t+=delta_t

