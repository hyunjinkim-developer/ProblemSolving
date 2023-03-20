#include <iostream>
#define MOD 1000000000

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	// Get input
	int N;
	cin >> N;
	if (!(1 <= N && N <= 100))
	{
		cout << "Not valid N.\n";
		return -1;
	}

	auto arr = new int [N+1][11];

	for (int i = 0; i <= 9; i++)
		arr[1][i] = 1; // the digit furthest to right

	for (int row = 2; row <= N; row++)
	{
		/* to make this row's digit to 0 
		   previous row's digit should be 1 */
		arr[row][0] = arr[row-1][1]; 
		/* to make this row's digit to 9
		   previous row's digit should be 1
		   tricks for making this tactic possible */
		arr[row][10] = 0;
		for (int col = 1; col <= 9; col++)
		{
			arr[row][col] = (arr[row-1][col-1] + arr[row-1][col+1]) % MOD;
		}
	}

	int answer = 0;
	for (int i = 1; i <= 9; i++)
	{
		answer = (answer + arr[N][i]) % MOD;
	}
	cout << answer;
	
	return 0;
}
