/* 
   Top Down
	Other's code
	https://gusrl4025.tistory.com/10
*/
#include <iostream>
#include <cmath>

using namespace std;

int top_down(int n, int *dp)
{
	if (n == 0)
		return 0;
	if (dp[n] > 0)
		return dp[n];

	dp[n] = top_down(n - 1, dp) + 1; // Initialize dp array
	for(int i = 1; i * i <= n; ++i)
	{
		dp[n] = min(dp[n], top_down(n - i * i, dp) + 1);
	}
	return dp[n];
}

int main(void)
{
	int N;
	scanf("%d", &N);

	int *dp = new int[N + 1];
	
	printf("%d", top_down(N, dp));

	return 0;
}
