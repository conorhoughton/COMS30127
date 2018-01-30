
function add_to_int(a::Integer,b::Integer)
	 println("int version")
	 a+b
end

function add_to_int(a::Real,b::Real)
	 println("float version")
	 convert(Int64,a+b)
end

function add_to_int(a,b)
	 println("what are these things")
	 0
end

println(add_to_int(12,6))
println(add_to_int(12.0,6.0))
println(add_to_int("twelve","six"))