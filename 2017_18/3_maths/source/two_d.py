
def df_dt(f,w):
    return -(f+w)/2

def dw_dt(f,w):
    return -w


delta_t=0.01

t=0
t_final=40.0

f=10
w=2

tau=3.0

while t<t_final:
    old_w,old_f=(w,f)
    f+=delta_t*df_dt(old_f,old_w)
    w+=delta_t*dw_dt(old_f,old_w)

    print t,f,w
    t+=delta_t
