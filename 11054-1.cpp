#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);
	int input[N];
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &input[i]);
	}
	int increase[N];
	int decrease[N];
	int bitonic_seq[N];

	// Find increasing sequence
	for (int i = 0; i < N; i++)
	{
		increase[i] = 1;
		for (int j = 0; j < i; j++)
		{
			// Update increase sequence count result only when it's needed
			// faster than 11054.cpp
			if (input[j] < input[i] && increase[j] + 1 > increase[i])
			{
				increase[i] = increase[j] + 1;
			}
		}
	}

	// Find decreasing sequence
	for (int i = N - 1; i >= 0; i--)
	{
		decrease[i] = 1;
		for (int j = N - 1; j > i; j--)
		{
			// Update decrease sequence count result only when it's needed
			// faster than 11054.cpp
			if (input[i] > input[j] && decrease[j] + 1 > decrease[i])
			{
				decrease[i] = decrease[j] + 1;
			}
		}
	}
	
	// Find max bitonic subsequence
	// using increasing sequence and decresing sequence
	int answer = 0;
	for (int i = 0; i < N; i++)
	{
		// ith number is both counted in decrease and increase sequence
		answer = max(answer, decrease[i] + increase[i] - 1);	
	}
	printf("%d", answer);

	return 0;
}
