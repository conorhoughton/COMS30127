#include <iostream>
#include <cmath>


double alphaN(double v)
{
  return .01*(v+55)/(1-std::exp(-.1*(v+55)));
}


double betaN(double v)
{
  return .125*std::exp(-.0125*(v+65));
}


double alphaM(double v)
{
  return .1*(v+40)/(1-std::exp(-.1*(v+40)));
}


double betaM(double v)
{
  return 4*std::exp(-.0556*(v+65));
}


double alphaH(double v)
{
  return .07*std::exp(-.05*(v+65));
}


double betaH(double v)
{
  return 1/(1+std::exp(-.1*(v+35)));
}





int main(){


  for(double v=-100;v<20;v++)
    {
      std::cout<<v<<"\t";
      std::cout<<alphaN(v)<<"\t"<<betaN(v)<<"\t"<<1/(alphaN(v)+betaN(v))<<"\t"<<alphaN(v)/(alphaN(v)+betaN(v))<<"\t";
      std::cout<<alphaM(v)<<"\t"<<betaM(v)<<"\t"<<1/(alphaM(v)+betaM(v))<<"\t"<<alphaM(v)/(alphaM(v)+betaM(v))<<"\t";
      std::cout<<alphaH(v)<<"\t"<<betaH(v)<<"\t"<<1/(alphaH(v)+betaH(v))<<"\t"<<alphaH(v)/(alphaH(v)+betaH(v))<<"\n";
    }


}
