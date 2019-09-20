#include<stdio.h>
int main(void)
{
    int input,x,y,n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&input);
        x=1;
        y=0;
    	while((input/x)>0)
        	{
        		x=x*5;
        		y=y+(input/x);
        	}
        	printf("%d\n",y);
    }
    return 0;
}
