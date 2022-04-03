// Did not pass time limit
#include <iostream>

using namespace std;

int main(void)
{
	// Get input
	int n;
	scanf("%d", &n);
	int *input = new int[n];
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &input[i]);
	}

	// Find biggest among sum of continued subsequence
	int answer = -1e8; // min 1e5(n) * -1e3(input number)
	int sum;
	for (int i = 0; i < n; i++)
	{
		printf("%d\n", i);
		sum = 0;
		for (int j = i; j < n; j++)
		{
			printf("%d ", j);
			sum += input[j];
			answer = sum > answer ? sum : answer;
		}
		printf("\n");
	}
	printf("%d", answer);

	delete input;
	return 0;
}
