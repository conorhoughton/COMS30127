# this shows the runge-kutta method with a harder example than the
# growth equation
# df/dt=f-t^2+1 // f(0)=0.5
# the exact solution is t^2+2t+1-e^t/2
# I took this example from 
# https://math.okstate.edu/people/yqwang/teaching/math4513_fall11/Notes/rungekutta.pdf

from math import *

def solution(t):
    return t*t+2*t+1-exp(t)/2


def example_g(t,f):
    return f-t*t+1

def rk_values(big_g,f,t,delta_t):

    k_1=big_g(t,f)*delta_t;
    k_2=big_g(t+delta_t/2,f+0.5*k_1)*delta_t;
    k_3=big_g(t+delta_t/2,f+0.5*k_2)*delta_t;
    k_4=big_g(t+delta_t,f+k_3)*delta_t;

    return (k_1+2*k_2+2*k_3+k_4)/6.0

t=0.0

delta_t=0.05

t_final=3.75


f_rk=0.5
f_euler=0.5

#note how functions are just objects
this_g=example_g

while t<=t_final:
    print t,f_rk,f_euler,solution(t)
    f_rk+=rk_values(this_g,f_rk,t,delta_t)
    f_euler+=example_g(t,f_euler)*delta_t
    t+=delta_t

#you could change this to plot the values
#I tend to use gnuplot for short programmes like this, not least because it produces nice graphs
#and can be exported using epslatex into a latex based format.
#
#to do it that way write "rk.py > f.dat" to pipe the results into a file "f.dat"
#then "gnuplot"
#then in gnuplot: 
#plot "f.dat" us 1:2 w lines title "rk"
#replot "f.dat" us 1:3 w lines title "euler"
#replot "f.dat" us 1:4 w lines title "exact"
#
#or to see the errors
#plot "f.dat" us 1:(($2)-($4)) w lines title "rk error"
#replot "f.dat" us 1:(($3)-($4)) w lines title "rk error"
#
#all this assume you are running *nix and have gnuplot installed
