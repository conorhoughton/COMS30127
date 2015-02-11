#ifndef HH_NEURON_H
#define HH_NEURON_H

#include "Neuron.hpp"

class HH_Neuron: public Neuron
{
  
public:
  

  HH_Neuron(double deltaT,double tauM, double eL, double eK, double eNa, double gKMax, double gNaMax);

  double getN(){return n;}
  double getM(){return m;}
  double getH(){return h;}

  double getIM() {return iM;}
  double getIL() {return iL;}
  double getINa(){return iNa;}
  double getIK() {return iK;}

  double operator+(const double & electrode);

private:

  double eK;
  double eNa;

  double n;
  double m;
  double h;

  double gKMax;
  double gNaMax;

  double alphaN(double v){return 1000*.01*(v+55)/(1-std::exp(-.1*(v+55)));}
  double betaN(double v){return 1000*.125*std::exp(-.0125*(v+65));}

  double alphaM(double v){return 1000*.1*(v+40)/(1-std::exp(-.1*(v+40)));}
  double betaM(double v){return 1000*4*std::exp(-.0556*(v+65));}

  double alphaH(double v){return 1000*.07*std::exp(-.05*(v+65));}
  double betaH(double v){return 1000*1/(1+std::exp(-.1*(v+35)));}

  double tau(double alpha,double beta){return 1/(alpha+beta);}
  double asym(double alpha,double tau){return alpha*tau;}

  double gateEqn(double init,double alpha,double beta);

  double iM,iNa,iK,iL;
   
};

#endif
