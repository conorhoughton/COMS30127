

function get_spike_train(rate::Float64,big_t::Float64,tau_ref::Float64)

    if 1<=rate*tau_ref
        println("firing rate not possible given refractory period f/p")
        return Float64[]
    end

    exp_rate=rate/(1-tau_ref*rate)

    spike_train=Vector{Float64}(0)

    t=randexp(Float64)/exp_rate

    while t< big_t
        push!(spike_train,t)
        t+=tau_ref+randexp(Float64)/exp_rate
    end

    spike_train

end

Hz=1.0::Float64
sec=1.0::Float64
ms=0.001::Float64

rate=15.0 *Hz
tau_ref=5*ms

big_t=5*sec

spike_train=get_spike_train(rate,big_t,tau_ref)

println(length(spike_train)/big_t)

println(spike_train)
