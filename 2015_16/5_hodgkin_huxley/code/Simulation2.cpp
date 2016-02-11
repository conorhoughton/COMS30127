#include <iostream>
#include <cmath>


#include "HH_Neuron.hpp"
#include "IF_Neuron.hpp"
#include "Electrode.hpp"

int main(){

  double mS=.0001;
  double deltaT=.025*mS;

  double tauM=10*mS;


  double eL=-54.387;

  double eK=-77;
  double eNa=50;

  double gL=.003;
  double gKMax=.36;
  double gNaMax=1.2;

  gKMax/=gL;
  gNaMax/=gL;

  HH_Neuron neuron(deltaT,tauM,eL,eK,eNa,gKMax,gNaMax);

  double onset1=0*mS;
  double offset1=0*mS;
  double onset2=100*mS;
  double offset2=500*mS;

  double amplitude1=0;
  double amplitude2=6;

  Electrode electrode(deltaT,onset1,offset1,onset2,offset2,amplitude1,amplitude2);
  

  double totalTime=500*mS;
  double time=0;

  while(time<totalTime)
    {
      double electrodeValue=electrode++;

      std::cout<<time<<"\t";
      std::cout<<electrodeValue<<"\t"<<neuron+(electrodeValue)<<"\t";
      std::cout<<neuron.getN()<<"\t"<<neuron.getM()<<"\t"<<neuron.getH()<<"\t";
      std::cout<<neuron.getINa()<<"\t"<<neuron.getIK()<<"\t"<<neuron.getIL()<<"\t";
      std::cout<<-neuron.getIK()<<"\t"<<neuron.getIM()<<"\t"<<neuron.getIM()/300<<"\t";
      std::cout<<pow(neuron.getN(),4)<<"\t"<<std::pow(neuron.getM(),3)*neuron.getH()<<std::endl;

      time+=deltaT;
    }

}
  




			    
