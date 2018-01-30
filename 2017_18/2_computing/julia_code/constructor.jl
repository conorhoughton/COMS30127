

struct Joke

    question::String
    answer::String

    function Joke(question::String,answer::String)
        if question[end]!="?"
            question=string(question,"?")
        end
        new(question,answer)
    end

end

function make_joke()
    Joke("what weapon does a fat jedi use","a heavy sabre")
end

joke=make_joke()

println(joke.question)
println(joke.answer)
