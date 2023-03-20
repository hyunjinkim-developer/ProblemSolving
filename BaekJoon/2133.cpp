// Bottom Up
#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);

	int answer = 0;
	int *format = new int[N / 2 + 1];
	format[0] = 1;
	format[1] = 3;
	if (N % 2 == 0) // N is even number;
	{
		for (int i = 2; i <= N / 2; ++i)
		{
			for (int j = 1; j <= i; ++j)
			{
				if (j == 1)
					format[i] += 3 * format[i - j];
				else
					format[i] += 2 * format[i - j];
			}
		}
		answer = format[N / 2];
	}
	else // N is odd number
	{
		answer = 0;
	}
	printf("%d", answer);

	delete[] format;
	return 0;
}
