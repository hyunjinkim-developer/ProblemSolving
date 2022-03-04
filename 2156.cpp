#include <iostream>

using namespace std;

int TopDown(int *wine, int *dp, int n)
{
	int &ret = dp[n];
	if (n < 1)
		return 0;
	if (n == 1)
		return ret = wine[1];
	if (n == 2)
		return  ret= wine[1] + wine[2];
	if (ret != -1)
		return ret;

	return ret = max(max(TopDown(wine, dp, n - 3) + wine[n] + wine[n - 1], TopDown(wine, dp, n - 2) + wine[n]), TopDown(wine, dp, n - 1)); 
}

int BottomUp(int *wine, int *dp, int n)
{
	dp[1] = wine[1];
	dp[2] = wine[1] + wine[2];

	for (int i = 3; i <= n; i++)
	{
		dp[i] = max(max(dp[i - 3] + wine[i] + wine[i - 1], dp[i - 2] + wine[i]), dp[i - 1]);
	}
	return dp[n];
}

int main(void)
{
	// Getting input
	int n;
	cin >> n;
	if (!(1 <= n && n <= 10000))
	{
		cout << "Not valid n.\n";
		return -1;
	}
	int *wine = new int[n + 1];
	int *dp = new int[n + 1];
	int input;
	for (int i = 1; i <= n; i++)
	{
		cin >> input;
		if (!(0 <= input && input <= 1000))
		{
			cout << "Not valid input amount.\n";
			return -1;
		}
		wine[i] = input;
		dp[i] = -1;
	}
	
	cout << TopDown(wine, dp, n);
	cout << endl;
	cout << BottomUp(wine, dp, n);

	return 0;
}
