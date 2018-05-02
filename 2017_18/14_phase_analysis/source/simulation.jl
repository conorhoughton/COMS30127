using DifferentialEquations

function asy(va::Float64,vb::Float64)
    return v::Float64->0.5*(1+tanh((v-va)/vb))
end

function tau(va::Float64,vb::Float64,phi::Float64)
    return v::Float64->1/(phi*cosh((v-va)/(2*vb)))
end

function make_v_nullcline(el::Float64,gca::Float64,m_inf::Function,eca::Float64,gk::Float64,ek::Float64,ie::Float64)
    return v::Float64->-(el-v+gca*m_inf(v)*(eca-v)+ie)/(gk*(ek-v))
end


function make_dv(el::Float64,gca::Float64,m_inf::Function,eca::Float64,gk::Float64,ek::Float64,ie::Float64,tau_m::Float64)
    function dv(v::Float64 , n::Float64)
        (el-v+gca*m_inf(v)*(eca-v)+ie+gk*n*(ek-v))/tau_m
    end

    return dv

end

function make_dn(n_inf::Function,tau_n::Function)
    dn(v::Float64, n::Float64)=(n_inf(v)-n)/tau_n(v)
end

function make_derivative(dv::Function,dn::Function)
    function derivative(dvn,vn,p,t)
        dvn[1]=dv(vn[1],vn[2])
        dvn[2]=dn(vn[1],vn[2])
    end

    return derivative

end


mv=0.001::Float64
ms=0.001::Float64
kHz=1000.::Float64

el=-60*mv::Float64
gca=2.2::Float64
eca=120*mv::Float64
gk=4.::Float64
ek=-84*mv::Float64
v1=-1.2*mv::Float64
v2=18*mv::Float64
v3=2*mv::Float64
v4=30*mv::Float64
phi=0.04.*kHz::Float64
ie=60.0*mv::Float64
tau_m=10*ms::Float64

m_inf=asy(v1,v2)
n_inf=asy(v3,v4)
tau_n=tau(v3,v4,phi)

v_nullcline=make_v_nullcline(el,gca,m_inf,eca,gk,ek,ie)

v=-60*mv::Float64

while v<55*mv
#    println(v," ",v_nullcline(v)," ",n_inf(v))
    v+=1*mv
end


dv=make_dv(el,gca,m_inf,eca,gk,ek,ie,tau_m)
dn=make_dn(n_inf,tau_n)

dvn=make_derivative(dv,dn)

vn0=[-40*mv,0.0]
tspan = (0.0,5.0)
prob = ODEProblem(dvn,vn0,tspan)
sol = solve(prob,savat=0.1)    


for (i,t) in enumerate(sol.t)
    println(t," ",sol[i][1]," ",sol[i][2])
end
