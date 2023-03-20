/*
	important!
	When variable is assigned to another variable with different type,
	first 'CAST' and then assign   
*/

#include <iostream>

using namespace std;

int N, M;

// Split in | | shape
long long splitCol(int **input)
{
	long long answer = 0;
	int sumFir, sumSec, sumThir; // Sum of each rectangle
	long long temp;

	for (int i = 1; i <= M - 2; i++)
	{
		sumFir = 0;
		for (int first = 0; first < i; first++)
		{
			for (int row = 0; row < N; row++)
			{
				sumFir += input[row][first];
			}
		}
		for (int j = i + 1; j < M; j++)
		{
			sumSec = 0;
			sumThir = 0;
			for (int second = i; second < j; second++)
			{
				for (int row = 0; row < N; row++)
				{
					sumSec += input[row][second];
				}
			}
			for (int third = j; third < M; third++)
			{
				for (int row = 0; row < N; row++)
				{
					sumThir += input[row][third];
				}
			}

			temp = (long long) sumFir * sumSec * sumThir;
			answer = max(temp, answer);  
		}
	}
	return answer;
}

// Split in = shape
long long splitRow(int **input)
{
	long long answer = 0;
	int sumFir, sumSec, sumThir; // Sum of each rectangle
	long long temp;

	for (int i = 1; i <= N - 2; i++)
	{
		sumFir = 0;
		for (int first = 0; first < i; first++)
		{
			for (int col = 0; col < M; col++)
			{
				sumFir += input[first][col];
			}
		}
		for (int j = i + 1; j < N; j++)
		{
			sumSec = 0;
			sumThir = 0;
			for (int second = i; second < j; second++)
			{
				for (int col = 0; col < M; col++)
				{
					sumSec += input[second][col];
				}
			}
			for (int third = j; third < N; third++)
			{
				for (int col = 0; col < M; col++)
				{
					sumThir += input[third][col];
				}
			}
			temp = (long long) sumFir * sumSec * sumThir;
			answer = max(temp, answer);  
		}
	}
	return answer;
}


int main(void)
{
	// Get input
	cin >> N >> M;
	
	int **input = new int *[N];
	for (int i = 0; i < N; i++)
	{
		input[i] = new int[M];
	}
	// A single digit number can go into each square
	string in;
	for (int i = 0; i < N; i++)
	{
		cin >> in;
		for (int j = 0; j< M; j++)
		{
			input[i][j] = in[j] - '0';
		}
	}

	int sumFir, sumSec, sumThir;
	long long answer = 0;
	long long temp;

	// Split into 3 rectangles
	if (N == 1) // 1 * M matrix
	{
		answer = splitCol(input);
	}
	else if (M == 1) // M * 1 matrix
	{
		answer = splitRow(input);
	}
	else // M * N matrix
	{
		// Split in ㅏ shape
		for (int splitCol = 1; splitCol < M; splitCol++)
		{
			// Left hand rectangle
			sumFir = 0;
			for (int col = 0; col < splitCol; col++)
			{
				for (int row = 0; row < N; row++)
				{
					sumFir += input[row][col];
				}
			}

			for (int splitRow = 1; splitRow < N; splitRow++)
			{
				// Right up rectangle
				sumSec = 0;
				for (int row = 0; row < splitRow; row++)
				{
					for (int col = splitCol; col < M; col++)
					{
						sumSec += input[row][col];
					}
				}
				
				// Right down rectangle
				sumThir = 0;
				for (int row = splitRow; row < N; row++)
				{
					for (int col = splitCol; col < M; col++)
					{
						sumThir += input[row][col];
					}
				}
				temp = (long long) sumFir * sumSec * sumThir;
				answer = max(temp, answer);  
			}
		}
	
		// Split in ㅓshape
		for (int splitCol = 1; splitCol < M; splitCol++)
		{
			// Right rectangle
			sumFir = 0;
			for (int col = splitCol; col < M; col++)
			{
				for (int row = 0; row < N; row++)
				{
					sumFir += input[row][col];
				}
			}

			for (int splitRow = 1; splitRow < N; splitRow++)
			{
				// Left up rectangle
				sumSec = 0;
				for (int row = 0; row < splitRow; row++)
				{
					for (int col = 0; col < splitCol; col++)
					{
						sumSec += input[row][col];
					}
				}

				// Left down rectangle
				sumThir = 0;
				for (int row = splitRow; row < N; row++)
				{
					for (int col = 0; col < splitCol; col++)
					{
						sumThir += input[row][col];
					}
				}
				temp =  (long long) sumFir * sumSec * sumThir;
				answer = max(temp, answer);  
			}
		}

		// Split in ㅜ shape
		for (int splitRow = 1; splitRow < N; splitRow++)
		{
			// Up rectangle
			sumFir = 0;
			for (int row = 0; row < splitRow; row++)
			{
				for (int col = 0; col < M; col++)
				{
					sumFir += input[row][col];
				}	
			}

			for (int splitCol = 1; splitCol < M; splitCol++)
			{
				// Down left rectangle
				sumSec = 0;
				for (int col = 0; col < splitCol; col++)
				{
					for (int row = splitRow; row < N; row++)
					{
						sumSec += input[row][col];
					}
				}

				// Down right rectangle
				sumThir = 0;
				for (int col = splitCol; col < M; col++)
				{
					for (int row = splitRow; row < N; row++)
					{
						sumThir += input[row][col];
					}
				}
				temp = (long long) sumFir * sumSec * sumThir;
				answer = max(temp, answer);  
			}
		}


		// Split in ㅗ shape
		for (int splitRow = 1; splitRow < N; splitRow++)
		{
			// Down rectangle
			sumThir = 0;
			for (int row = splitRow; row < N; row++)
			{
				for (int col = 0; col < M; col++)
				{
					sumThir += input[row][col];
				}
			}

			for (int row = 0; row < splitRow; row++)
			{
				for (int splitCol  = 1; splitCol < M; splitCol++)
				{
					// Up left rectangle
					sumFir = 0;
					for (int col = 0; col < splitCol; col++)
					{
						for (int row = 0; row < splitRow; row++)
						{
							sumFir += input[row][col];
						}
					}

					// Up right rectangle
					sumSec = 0;
					for (int col = splitCol; col < M; col++)
					{
						for (int row = 0; row < splitRow; row++)
						{
							sumSec += input[row][col];
						}
					}
					temp = (long long) sumFir * sumSec * sumThir;
					answer = max(temp, answer);  
				}
			}
		}

		// Split in | | shape
		answer = max(answer, splitCol(input));

		// Split in = shape
		answer = max(answer, splitRow(input));
	}

	cout << answer;

	return 0;
}
