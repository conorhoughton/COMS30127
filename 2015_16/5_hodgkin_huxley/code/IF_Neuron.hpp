#ifndef IF_NEURON_H
#define IF_NEURON_H

#include "Neuron.hpp"

class IF_Neuron: public Neuron
{
  
public:
  
  IF_Neuron(double deltaT,double tauM,double vReset,double vThreshold, double eL);

  double operator+(const double & electrode);

private:

  double vReset;
  double vThreshold;
   
};

#endif
