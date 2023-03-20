#include <iostream>

using namespace std;

int N, M;

// Sum rectangles from (startRow, startCol) to (endRow - 1, to endCol - 1)
// Range [start, end)
int sum(int startR, int endR, int startC, int endC, int **input)
{
	int sum = 0;
	for (int row = startR; row < endR; row++)
	{
		for (int col = startC; col < endC; col++)
		{
			sum += input[row][col];
		}
	}
	return sum;
}

long long getMax(int **input)
{
	long long ans = 0; // Max
	long long s1, s2, s3;

	// Split in | | shape
	// Row: [0, first], [first + 1, second], [second + 1, M)
	//  -> [0, first + 1), [first + 1, second + 1), [second + 1, M)
	for (int first = 0; first < M - 2; first++)
	{
		for (int second = first + 1; second < M - 1; second++)
		{
			s1 = sum(0, N, 0, first + 1, input);
			s2 = sum(0, N, first + 1, second + 1, input);
			s3 = sum(0, N, second + 1, M, input);
			ans = max(ans, s1 * s2 * s3);
		}
	}

	// Split in = shape
	// Col: [0, first], [first + 1, second], [second + 1, N)
	// -> [0, first + 1), [first + 1, second + 1), [second + 1, N)
	for (int first = 0; first < N - 2; first++)
	{
		for (int second = first + 1; second < N - 1; second++)
		{
			s1 = sum(0, first + 1, 0, M, input);
			s2 = sum(first + 1, second + 1, 0, M, input);
			s3 = sum(second + 1, N, 0, M, input);
			ans = max(ans, s1 * s2 * s3);
		}
	}

	// Split in ㅏ shape
	for (int col = 0; col < M - 1; col++)
	{
		for (int row = 0; row < N - 1; row++)
		{
			// Left
			s1 = sum(0, N, 0, col + 1, input);
			// Right up
			s2 = sum(0, row + 1, col + 1, M, input);
			// Right down
			s3 = sum(row + 1, N, col + 1, M, input);
			ans = max(ans, s1 * s2 * s3);
		}
	}

	// Split in ㅓ shape
	for (int col = 0; col < M - 1; col++)
	{
		for (int row = 0; row < N - 1; row++)
		{
			// Left up
			s1 = sum(0, row + 1, 0, col + 1, input);
			// Left down
			s2 = sum(row + 1, N, 0, col + 1, input);
			// Right
			s3 = sum(0, N, col + 1, M, input);
			ans = max(ans, s1 * s2 * s3);
		}
	}

	// Split in ㅜ shape 
	for (int col = 0; col < M - 1; col++)
	{
		for (int row = 0; row < N - 1; row++)
		{
			// Up
			s1 = sum(0, row + 1, 0, M, input);
			// Down left
			s2 = sum(row + 1, N, 0, col + 1, input);
			// Down right
			s3 = sum(row + 1, N, col + 1, M, input);
			ans = max(ans, s1 * s2 * s3);
		}
	}

	// Split in ㅗ shape
	for (int col = 0; col < M - 1; col++)
	{
		for (int row = 0; row < N - 1; row++)
		{
			// Up left
			s1 = sum(0, row + 1, 0, col + 1, input);
			// Up right
			s2 = sum(0, row + 1, col + 1, M, input);
			// Down
			s3 = sum(row + 1, N, 0, M, input);
			ans = max(ans, s1 * s2 * s3);
		}
	}
	
	return ans;
}

int main(void)
{
	// Get inpupt
	cin >> N >> M;
	
	int **input = new int *[N];
	for (int i = 0; i < N; i++)
	{
		input[i] = new int [M];
	}
	string in; // Max input is in 50 digits
	for (int i = 0; i < N; i++)
	{
		cin >> in;
		for (int j = 0; j < M; j++)
		{
			input[i][j] = in[j] - '0';
		}
	}
	
	cout << getMax(input);

	return 0;
}
