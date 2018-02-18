
n=10

x_off=1.0
y_off=2.0

x=randn(10)+x_off*ones(10)
y=randn(10)+y_off*ones(10)

for i in 1:10
    println(x[i]," ",y[i])
end
