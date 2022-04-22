#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);

	for (int i = 0; i < 2 * N - 1; ++i)
	{
		if (i < N)
		{
			for (int j = 0; j < i; ++j)
			{
				printf(" ");
			}
			int star = (2 * N - 1) - 2 * i;
			for (int l = 0; l < star; ++l)
			{
				printf("*");
			}
			printf("\n");
		}
		else
		{
			for (int j = 0; j < 2 * N - 2 - i; ++j)
			{
				printf(" ");
			}
			for (int l = 0; l < (2 * (i - N + 1)) + 1; ++l)
			{
				printf("*");
			}
			printf("\n");
		}
	}
	return 0;
}
