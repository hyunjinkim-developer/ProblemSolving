#include <stdio.h>

using namespace std;

int main(void)
{
	int input;
	
	while ((input = getchar()) != EOF)
	{
		putchar(input); // much faster than printf because of simple functionality
	//	printf("%c", input);
	}
	return 0;
}
