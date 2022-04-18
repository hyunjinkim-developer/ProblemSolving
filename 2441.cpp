#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);

	for (int i = 0; i < N; ++i)
	{
		for (int j = 1; j <= i; ++j)
		{
			printf(" ");
		}
		for (int l = 1; l <= N - i; ++l)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
