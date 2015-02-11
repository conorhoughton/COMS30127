#ifndef NEURON_H
#define NEURON_H
 
class Neuron
{
 
public:

  Neuron(double deltaT,double tauM, double eL);
  


protected:

  double v;

  double deltaT;
  
  double tauM;

  double eL;
  


};

#endif
