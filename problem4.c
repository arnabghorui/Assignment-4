//Transformation method
#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
int main()
{
	int N = 10000;
	double x,y;

	FILE *data;
	data = fopen("problem4.txt", "w");
	for (int i = 0; i < N; ++i)
	{
		x = rand() / (double)RAND_MAX;
		y = -0.5*log(x);
		fprintf(data, "%lf\n", y);
	}
	fclose(data);
return 0;
}