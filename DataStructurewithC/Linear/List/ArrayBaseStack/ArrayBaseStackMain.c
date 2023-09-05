#include <stdio.h>

#include "ArrayBaseStack.h"

int main(void)
{
	// Create stack and Initialize it
	Stack stack;
	StackInit(&stack);

	// Save data
	SPush(&stack, 1);
	SPush(&stack, 2);
	SPush(&stack, 3);
	SPush(&stack, 4);
	SPush(&stack, 5);

	// Remove all of data
	while (!SIsEmpty(&stack))
	{
		printf("%d ", SPop(&stack));
	}

	return 0;
}

