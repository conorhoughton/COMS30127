#include <iostream>
#include <cmath>
 
#include "HH_Neuron.hpp"

HH_Neuron::HH_Neuron(double deltaT,double tauM, double eL,
		       double eK, double eNa, double gKMax, double gNaMax)
  :Neuron(deltaT, tauM, eL)
{
  this->eK=eK;
  this->eNa=eNa;

  this->gKMax=gKMax;
  this->gNaMax=gNaMax;
  
  v=eL;

  n=asym(alphaN(v),tau(alphaN(v),betaN(v)));
  m=asym(alphaM(v),tau(alphaM(v),betaM(v)));
  h=asym(alphaH(v),tau(alphaH(v),betaH(v)));


}


double HH_Neuron::operator+(const double & electrode)
{
  

  iM=eL-v+gKMax*std::pow(n,4)*(eK-v)+gNaMax*std::pow(m,3)*h*(eNa-v);
  iL=eL-v;
  iK=gKMax*std::pow(n,4)*(eK-v);
  iNa=gNaMax*std::pow(m,3)*h*(eNa-v);

  v+=(iM+electrode)*deltaT/tauM;
  n=gateEqn(n,alphaN(v),betaN(v));
  m=gateEqn(m,alphaM(v),betaM(v));
  h=gateEqn(h,alphaH(v),betaH(v));

  return v;

}


double HH_Neuron::gateEqn(double init,double alpha,double beta){
    double tau=HH_Neuron::tau(alpha,beta);
    double asym=HH_Neuron::asym(alpha,tau); 
    return asym+(init-asym)*std::exp(-deltaT/tau);
}
