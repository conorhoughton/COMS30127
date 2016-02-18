#include <iostream>
#include <cmath>
 
#include "IF_Neuron.hpp"

IF_Neuron::IF_Neuron(double deltaT,double tauM,double vReset,double vThreshold, double eL)
  :Neuron(deltaT,tauM,eL)
{
  this->vReset=vReset;
  this->vThreshold=vThreshold;
  v=vReset;

}

double IF_Neuron::operator+(const double & electrode)
{

  v=(eL+electrode)+(v-eL-electrode)*std::exp(-deltaT/tauM);

  if(v>vThreshold)
    {
      v=vReset;
      return 0;
    }

  return v;

}
