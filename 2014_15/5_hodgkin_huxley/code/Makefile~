
sim : Simulation.o Electrode.o  IF_Neuron.o HH_Neuron.o Neuron.o
	g++ -o sim Simulation.o Electrode.o IF_Neuron.o HH_Neuron.o Neuron.o


Simulation.o: Simulation.cpp 
	g++ -Wall -pedantic -ansi -O -c Simulation.cpp


Electrode.o: Electrode.cpp Electrode.hpp
	g++ -Wall -pedantic -ansi -O -c Electrode.cpp


HH_Neuron.o: HH_Neuron.cpp HH_Neuron.hpp
	g++ -Wall -pedantic -ansi -O -c HH_Neuron.cpp



IF_Neuron.o: IF_Neuron.cpp IF_Neuron.hpp
	g++ -Wall -pedantic -ansi -O -c IF_Neuron.cpp


Neuron.o: Neuron.cpp Neuron.hpp
	g++ -Wall -pedantic -ansi -O -c Neuron.cpp
