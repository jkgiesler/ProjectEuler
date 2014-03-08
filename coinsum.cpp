#include <iostream>
/*still very much a work in progress */

int main()
{
	using namespace std;
	double ans=0;
	double count=0;
	double it=0;
	double tot = 7.2e11;
	double test;
	for(int i=0;i<2000;i++)//1p
	{
		for(int j=0;j<1000;j++)//2p
		{
			for(int k=0;k<200;k++)//5p
			{
				for(int l=0;l<20;k++)//10p
				{
					for(int m=0;m<20;m++)//20p
					{
						for(int n=0;n<6;n++)//50p
						{
							for(int o=0;o<5;o++)//1000
							{
								for(int p=0;p<3;p++)//2000
								{
									test=1*i+2*j+5*k+10*l+20*m+n*50+o*1000+p*2000;
									if (test==2000)
									{
										count++;
										
									}
									it++;
									cout<<it/tot<<endl;
								}
							}
						}
					}
				}
			}
		}
	}
		
	cout<<count<<endl;

	return 0;

}
