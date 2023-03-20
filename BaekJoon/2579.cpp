// Top Down
#include <cstring>
#include <iostream>

using namespace std;

int recursive(int *input, int *dp, int idx)
{
	if (dp[idx] == -1)
	{
		dp[idx] = max(recursive(input, dp, idx - 2), recursive(input, dp, idx - 3) + input[idx - 1]) + input[idx];
	}

	return dp[idx];
}


int main(void)
{
	// Get input
	int N;
	scanf("%d", &N);
	int *input = new int[N + 1];
	for (int i = 1; i <= N; i++)
	{
		scanf("%d", &input[i]);
	}
	int *dp = new int[N + 1]; // BOJ does not accept int *dp = new int(N + 1);
	memset(dp, -1, (N + 1) * sizeof(int));	
	dp[0] = input[0];
	dp[1] = input[1];
	if (N >= 2)
		dp[2] = input[1] + input[2];

	printf("%d", recursive(input, dp, N));

	return 0;
}
