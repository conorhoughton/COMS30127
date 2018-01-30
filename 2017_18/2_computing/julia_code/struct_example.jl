
mutable struct Cow
	name::String
	age::Int64
end

mutable struct Poem
	name::String
end	

function move(cow::Cow)
	 println(cow.name," walks forward showing the weight of her ",cow.age," years")
end

function move(poem::Poem)
	 println(poem.name, " moves us to tears with its beauty")
end

poem = Poem("The Red Wheelbarrow")
cow = Cow("Hellcow",42)

move(cow)
move(poem)