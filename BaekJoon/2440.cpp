#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);

	for (int i = 0; i < N; ++i)
	{
		for (int j = 1; j <= N - i; j++)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
