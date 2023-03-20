// Top Down with memoization
// Bottom UP
// Using Bottom Up is faster than using top down approach

#include <iostream>

using namespace std;

int top_down(int y, int x, int **input, int **dp)
{
	if (x < 0)
		return 0;
	int &ret = dp[y][x];
	if(ret != -1) 
		return ret;

	if (y == 0)
		return ret = max(top_down(1, x - 1, input, dp), top_down(1, x - 2, input, dp)) + input[0][x];
	if (y == 1)
		return ret = max(top_down(0, x - 1, input, dp), top_down(0, x - 2, input, dp)) + input[1][x];
}

int bottom_up(int n, int **input, int **dp)
{
	dp[0][1] = input[0][1];
	dp[1][1] = input[1][1];
	dp[0][2] = input[1][1] + input[0][2];
	dp[1][2] = input[0][1] + input[1][2];

	for (int i = 3; i <= n; i++)
	{
		dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + input[0][i];
		dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + input[1][i];
	}

	return max(dp[0][n], dp[1][n]);
}

int main(void)
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n;
		cin >> n;
		int **input = new int *[2];
		int **dp = new int *[2];
		for (int i = 0; i < 2; i++)
		{
			input[i] = new int[n + 1];
			dp[i] = new int[n + 1];
			for (int j = 1; j <= n; j++)
			{
				cin >> input[i][j];
				dp[i][j] = -1;
			}
		}

		// Top Down
		cout << max(top_down(0, n, input, dp), top_down(1, n, input, dp)) << '\n';

		// Bottom Up
		cout << bottom_up(n, input, dp) << '\n';
	}
	return 0;
}
