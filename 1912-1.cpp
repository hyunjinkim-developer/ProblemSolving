#include <iostream>

using namespace std;

int main(void)
{
	int n;
	scanf("%d", &n);
	int *input = new int[n];
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &input[i]);
	}

	int answer = -1e8;
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum += input[i];
		if (input[i] > sum)
			sum = input[i];

		answer = sum > answer ? sum : answer;
	}
	cout << answer;

	return 0;
}
