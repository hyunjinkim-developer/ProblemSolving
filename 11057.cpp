#include <iostream>

#define MOD 10007

using namespace std;

int main(void)
{
	int N;
	cin >> N;
	if (!(1 <= N && N <= 1000))
	{
		cout << "Not valid N.\n";
		return -1;
	}

	int **arr = new int *[N+1];
	for (int i = 0; i <= N + 1; i++)
	{
		arr[i] = new int[10];
	}
	for (int i = 0; i <= 9; i++)
	{
		arr[1][i] = 1;
	}

	int answer;
	for (int row = 1; row <= N; row++)
	{
		answer = 0;
		for (int col = 0; col <= 9; col++)
		{
			for (int i = col; i <= 9; i++)
			{
				arr[row][col] = (arr[row][col] + arr[row-1][i]) % MOD;
			}
			answer = (answer + arr[row][col]) % MOD;
		}
	}
	cout << answer;
	
	return 0;
}
