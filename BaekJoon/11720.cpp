#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);
	if (!(1 <= N && N <= 100))
	{
		printf("Not valid N.\n");
		return -1;
	}
	int sum = 0;
	char num[100];
	scanf("%s", num);
	for (int i = 0; i < N; i++)
	{
		sum += (num[i] - '0');
	}
	printf("%d", sum);

	return 0;
}
