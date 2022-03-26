// Using C standard io function is much safer and faster

#include <iostream>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++)
	{
		printf("%d\n", i);
	}

	return 0;
}
