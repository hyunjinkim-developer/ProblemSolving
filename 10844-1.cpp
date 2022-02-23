// Using Sliding Window Method
// to use less memory (using only 2 rows)

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
	
	int array[2][12] = {0};
	/*
		Tricks to make proper result for N is 2
		index    : 0 1 2 3 4 5 6 7 8 9 10 11
		digit#       0 1 2 3 4 5 6 7 8 9   
		array[0] : 0 1 1 2 2 2 2 2 2 2 1 0 -> result of N is 2
		array[1] : 0 0 1 1 1 1 1 1 1 1 1 0 
	*/
	for (int i = 2; i <= 10; i++)
		array[1][i] = 1;
	
	int answer = 9; // When N is 1
	for (int row = 2; row <= N; row++)
	{
		answer = 0;
		for (int col = 1; col <= 10; col++)
		{
			array[row % 2][col] = (array[(row - 1) % 2][col - 1] + array[(row - 1) % 2][col + 1]) % MOD;
			answer = (answer + array[row % 2][col]) % MOD;
		}
	}
	cout << answer;

	return 0;
}
