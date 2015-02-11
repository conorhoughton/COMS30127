#include <iostream>
#include <cmath>

#include "Electrode.hpp"

Electrode::Electrode(double deltaT, double onset1,double offset1,double onset2,double offset2,double amplitude)
{
  this->deltaT=deltaT;
  this->onset1=onset1;
  this->offset1=offset1;
  this->onset2=onset2;
  this->offset2=offset2;
  this->amplitude1=amplitude;
  this->amplitude2=amplitude;
  t=0;
}


Electrode::Electrode(double deltaT, double onset1,double offset1,double onset2,
		     double offset2,double amplitude1,double amplitude2)
{
  this->deltaT=deltaT;
  this->onset1=onset1;
  this->offset1=offset1;
  this->onset2=onset2;
  this->offset2=offset2;
  this->amplitude1=amplitude1;
  this->amplitude2=amplitude2;
  t=0;
}

double Electrode::operator++(int)
{
  double iE=0; 
  if(t>onset1&&t<offset1)
    iE=amplitude1;
  else if(t>onset2&&t<offset2)
    iE=amplitude2;
  t+=deltaT;
  return iE;
  
}
