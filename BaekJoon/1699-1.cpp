// Bottom Up
#include <iostream>
#include <math.h>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);
	
	int *dp = new int[N + 1];
	int root;
	for (int i = 1; i <= N; i++)
	{
		dp[i] = i; // Max will be summation of all in 1*1
		root = sqrt(i);	
		for (int j = root; j > 0; j--)
		{
			dp[i] = min(dp[i], dp[i - j*j] + 1);
		}
	}
	printf("%d", dp[N]);

	delete[] dp;
	return 0;
}
