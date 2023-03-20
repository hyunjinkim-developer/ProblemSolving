/* 
   Using Dynamic Programming
   (a + b + c) % n = (((a + b) % n) + c) % n
 */
#include <iostream>

#define div 1000000000 //<-int, 1e9: double

using namespace std;

int main(void)
{
	int N, K;
	scanf("%d %d", &N, &K);
	
	int **dp = new int *[N + 1];
	for (int i = 0; i <= N; i++)
	{
		dp[i] = new int [K + 1]; 
	}
	for (int n = 1; n <= N; ++n)
	{
		dp[n][1] = 1;
	}
	for (int k = 1; k <= K; ++k)
	{
		dp[1][k] = k;
	}

	for (int k = 2; k <= K; ++k)
	{
		for (int n = 2; n <= N; n++)
		{
			dp[n][k] = (dp[n - 1][k] + dp[n][k - 1]) % div;
		}
	}
	
	printf("%d", dp[N][K]);
	return 0;
}
