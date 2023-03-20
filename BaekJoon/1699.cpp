// Top Down 
#include <iostream>
#include <math.h>

using namespace std;

void divide(int n, int answer, int *ret)
{
	if (n == 0)
	{
		*ret = answer < *ret ? answer : *ret;
		return ;
	}

	int root = (int) sqrt(n);
	for (int i = root; i > 0; --i)
	{
		if (answer + 1 < *ret)
			divide(n - pow(i, 2), answer + 1, ret);
		else
			return ;
	}
}

int main(void)
{
	int N;
	scanf("%d", &N); 

	int answer = 1e6; // B/c Max of N is 1e5
	divide(N, 0, &answer);
	printf("%d", answer);
	
	return 0;
}
