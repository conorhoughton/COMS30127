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
      y+=r*y*delta_t;
      t+=delta_t;
    }

}
