
function load_data(filename,T)

    file=open(filename)

    data_array=readdlm(file,T)

    data_array

end

spikes=load_data("rho.dat",Int64)

println(length(spikes))
println(spikes[1:5])

stimulus=load_data("stim.dat",Float64)

println(length(stimulus))
println(stimulus[1:5])
