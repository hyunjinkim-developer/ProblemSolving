#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);

	for (int i = 1; i <= N; ++i)
	{
		for (int j = N - i; j > 0; --j)
		{
			printf(" ");
		}
		for (int l = 1; l <= 2 * i - 1; ++l)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
