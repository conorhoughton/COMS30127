
highest_power=10

value=1.0::Float64
current=0.5::Float64

for i in 1:highest_power
   value+=current
   current*=0.5
end

println(value)