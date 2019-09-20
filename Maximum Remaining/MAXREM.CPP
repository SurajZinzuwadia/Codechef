#include <iostream>
using namespace std;

int main() {

		long int n;
	cin>>n;
	long long int a[n+1],max1=0,max2=0;
	for(int i=0;i<n;i++)
	{
	    cin>>a[i];
	    if(a[i]>max1)
	    {
	        max2=max1;
	        max1=a[i];
	    }
	    else if(a[i]>max2&&a[i]<max1)
	    max2=a[i];
	}
	cout<<max2<<endl;
	return 0;
}
