// Swap
#include <stdio.h>

int main(void)
{
	int a = 3;
	int b = 5;

	int temp = a;
	a = b;
	b = temp;

	printf("a: %d, b: %d", a, b);

	return 0;
}
