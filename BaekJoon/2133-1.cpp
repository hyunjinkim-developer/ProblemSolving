// Top Down
#include <iostream>

using namespace std;

int count(int n, int * format)
{
	if (n == 0)
		return 1;
	if (n == 1)
		return 3;
	if (format[n] != 0)
		return format[n];

	// Block that is length of 2 is added
	// 3 possible ways to make the block of 3 * 2 
	int temp = 3 * count(n - 1, format);
	for (int i = 2; i <= n; ++i)
	{
		// Block that is length of more than 2 is added
		// 2 possible ways to make the block of 3 * n (n > 2) 
		// which is up down symmetry
		temp += 2 * count(n - i, format);
	}
	
	return format[n] = temp;
}

int main(void)
{
	// Get input
	int N;
	scanf("%d", &N);

	int answer = 0;
	int *format = new int[N / 2 + 1];

	// Count possible tiles arrangement
	if (N % 2 == 0)
		answer = count(N / 2, format);
	else
		answer = 0;

	printf("%d", answer);
	
	delete[] format;
	return 0;
}
