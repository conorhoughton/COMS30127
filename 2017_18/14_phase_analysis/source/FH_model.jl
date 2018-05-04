using Plots

I = 0
a = 0.7
b = 0.8
tau = 12.5

vvec = collect(-2:0.01:2)
vnull = vvec -(1/3).*vvec.^3 + I
wnull = (vvec + a)./b

Plots.plot(vvec,vnull,label="dv/dt=0",xlabel="voltage, v",ylabel="recovery, v",linewidth=2,xlim=(-2,2),ylim=(-1,1.5))
Plots.plot!(vvec,wnull,label="dw/dt=0",linewidth=2)
savefig("ML_nullclines.png")

v0 = -0.1
w0 = 0.1
dt = 0.1
tvec = collect(0:dt:100)
trackv = Array{Float64}(length(tvec))
trackv[1] = v0
trackw[1] = w0
trackw = Array{Float64}(length(tvec))
i = 1
for i = 2:length(tvec)
    v = trackv[i-1]
    w = trackw[i-1]
    trackv[i] = v + (v -v^3/3 - w + I)*dt
    trackw[i] = w + ((v + a - b*w  )/tau)*dt
end


Plots.plot(tvec,trackv,xlabel="time",linewidth=2,label="v")
Plots.plot!(tvec,trackw,linewidth=2,label="w")
savefig("ML_v_and_w_vs_time.png")

Plots.plot(trackv,trackw,linecolor=:black,xlabel="voltage, v",ylabel="recovery, v",linewidth=2,fillalpha=0.0,xlim=(-2,2),ylim=(-1,1.5),label="")
savefig("ML_v_vs_w.png")
