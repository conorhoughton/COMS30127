#include<cstdlib>
#include<iostream>
#include<cmath>

using namespace std;

int main()
{
  double delta_t=0.2;

  double t=0;

  double y=1;

  double big_t=5;

  double r=0.5;

  while(t<=big_t)
    {
      cout<<t<<" "<<y<<" "<<exp(r*t)<<endl;
      double k_1=r*y;
      double k_2=r*(y+k_1*delta_t/2);
      double k_3=r*(y+k_2*delta_t/2);
      double k_4=r*(y+k_3*delta_t);
      y+=(k_1+2*k_2+2*k_3+k_4)*delta_t/6;
      t+=delta_t;
    }

}
