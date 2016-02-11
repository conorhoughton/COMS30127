#include <iostream>
#include <cmath>
 
#include "Neuron.hpp"

Neuron::Neuron(double deltaT,double tauM, double eL)
{
  this->deltaT=deltaT;
  this->tauM=tauM;
  this->eL=eL;
  v=eL;
}

