// Bottom Up
#include <iostream>

using namespace std;

int main(void)
{
	// Get input
	int T;
	scanf("%d", &T);
	int *input = new int[T];
	int num;
	int max_input = 0;
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &num);
		max_input = num > max_input ? num : max_input;
		input[i] = num;
	}

	long long *count = new long long[max_input];
	count[0] = 1;
	count[1] = 1;
	count[2] = 1;
	count[3] = 2;
	count[4] = 2;
	for (int i = 5; i < max_input; i++)
	{
		count[i] = count[i - 1] + count[i - 5];
	}

	for (int i = 0; i < T; i++)
	{
		printf("%lld\n", count[input[i] - 1]);
	}

	return 0;
}
