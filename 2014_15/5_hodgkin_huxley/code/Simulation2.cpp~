#include <iostream>
#include <cmath>


#include "HH_Neuron.hpp"
#include "IF_Neuron.hpp"
#include "Electrode.hpp"

int main(){

  double mS=.0001;
  double deltaT=.025*mS;

  double tauM=10*mS;
  double vReset=-65;
  double vThreshold=-50;

  double eL=-54.387;

  double eK=-77;
  double eNa=50;

  double gL=.003;
  double gKMax=.36;
  double gNaMax=1.2;

  gKMax/=gL;
  gNaMax/=gL;

  HH_Neuron neuron1(deltaT,tauM,eL,eK,eNa,gKMax,gNaMax);
  IF_Neuron neuron2(deltaT,tauM,vReset,vThreshold,eL);

  double onset1=0*mS;
  double offset1=0*mS;
  double onset2=100*mS;
  double offset2=400*mS;

  double amplitude1=27;
  double amplitude2=37;

  Electrode electrode(deltaT,onset1,offset1,onset2,offset2,amplitude1,amplitude2);
  

  double totalTime=500*mS;
  double time=0;

  while(time<totalTime)
    {
      double electrodeValue=electrode++;

      std::cout<<time<<"\t";
      std::cout<<neuron2+(electrodeValue)<<"\t"<<electrodeValue<<"\t"<<neuron1+(electrodeValue)<<"\t";
      std::cout<<neuron1.getN()<<"\t"<<neuron1.getM()<<"\t"<<neuron1.getH()<<"\t";
      std::cout<<neuron1.getINa()<<"\t"<<neuron1.getIK()<<"\t"<<neuron1.getIL()<<"\t";
      std::cout<<-neuron1.getIK()<<"\t"<<neuron1.getIM()<<"\t"<<neuron1.getIM()/300<<"\t";
      std::cout<<pow(neuron1.getN(),4)<<"\t"<<std::pow(neuron1.getM(),3)*neuron1.getH()<<std::endl;

      time+=deltaT;
    }

}
  




			    
