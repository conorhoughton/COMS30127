
function make_adder(a::Int64)
    b::Int64->a+b
end

three_adder=make_adder(3)
two_adder=make_adder(2)

println(two_adder(5)," ",three_adder(5))




  
