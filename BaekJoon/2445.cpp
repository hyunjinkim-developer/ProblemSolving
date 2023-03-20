#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);

	for (int i = 1; i < N; ++i)
	{
		for (int j = 1; j <= i; ++j)
		{
			printf("*");
		}
		for (int j = 2 * (N - i); j > 0; --j)
		{
			printf(" ");
		}
		for (int j = 1; j <= i; ++j)
		{
			printf("*");
		}
		printf("\n");
	}
	for (int i = 0; i < 2 * N; ++i)
	{
		printf("*");
	}
	printf("\n");
	for (int i = 1; i < N; ++i)
	{
		for (int j = N - i; j > 0; --j)
		{
			printf("*");
		}
		for (int j = 2 * i; j > 0; --j)
		{
			printf(" ");
		}
		for (int j = N - i; j > 0; --j)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
