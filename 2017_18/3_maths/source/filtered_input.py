
def input (t):
    if t<2:
        return 0
    if t<10:
        return 1
    if t<15:
        return 0
    if t<17:
        return 2
    if t<24:
        return 0
    if t<25:
        return 1
    if t<26:
        return 0
    if t<27:
        return 1
    if t<28:
        return 0
    if t<29:
        return 1
    if t<30:
        return 0
    if t<31:
        return 1
    if t<32:
        return 0
    if t<33:
        return 1
    if t<34:
        return 0
    if t<35:
        return 1
    if t<36:
        return 0
    if t<37:
        return 1


    return 0

delta_t=0.01

t=0
t_final=40.0

f=0.0

tau=3.0

while t<t_final:
    g_bar=input(t)
    f+=delta_t*(g_bar-f)/tau
    print t,f,g_bar
    t+=delta_t



