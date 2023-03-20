// Bottom Up
#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);
	int *input = new int[N];
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &input[i]);
	}
	int *dp = new int[N];
	dp[0] = input[0];
	dp[1] = input[0] + input[1]; // As input >= 0, input[0] +  input[1] > input[1] 
	dp[2] = max(input[0] + input[2], input[1] + input[2]);
	for (int i = 3; i < N; i++)
	{
		dp[i] = max(input[i] + input[i - 1] + dp[i - 3], input[i] + dp[i - 2]);
	}
	printf("%d", dp[N - 1]);

	return 0;
}
