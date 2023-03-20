// Top Down
#include <iostream>

using namespace std;

long long recursive(int n, long long *count)
{
	if (n == 0 || n == 1 || n == 2)
		return 1;
	if (n == 3 || n == 4)
		return 2;
	if (count[n] != 0)
		return count[n];

	return count[n] = recursive(n - 1, count) + recursive(n - 5, count);
}


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
	for (int i = 0; i < T; i++)
	{
		printf("%lld\n", recursive(input[i] - 1, count));
	}

	return 0;
}
