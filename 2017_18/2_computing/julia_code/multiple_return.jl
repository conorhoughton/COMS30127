function powers(x)
	 x,x^2,x^3
end

multiples(x::Float64) = x,2x,3x

a,b,c=powers(2)

println(a,' ',b,' ',c)

a,b,c=multiples(2.0)

println(a,' ',b,' ',c)
