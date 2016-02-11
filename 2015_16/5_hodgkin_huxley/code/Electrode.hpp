#ifndef ELECTRODE_H
#define ELECTRODE_H
 
class Electrode
{
 
public:
  Electrode(double deltaT, double onset1,double offset1,double onset2,double offset2,double amplitude1,double amplitude2);
  Electrode(double deltaT, double onset1,double offset1,double onset2,double offset2,double amplitude);

  double operator++(int);

private:

  double deltaT;

  double t;
  
  double onset1;
  double offset1;
  double onset2;
  double offset2;

  double amplitude1;
  double amplitude2;


};

#endif
