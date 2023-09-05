#include <stdio.h>

#include "ListBaseStack.h"

int main(void)
{
	// Create Stack and Initialize
	Stack stack;
	StackInit(&stack);

	// Save(Push) data
	SPush(&stack, 1);
	SPush(&stack, 2);
	SPush(&stack, 3);
	SPush(&stack, 4);
	SPush(&stack, 5);

	// Remove(Pop) data
	while(!SIsEmpty(&stack))
	{
		printf("Peek: %d ", SPeek(&stack));
		printf("Pop: %d\n", SPop(&stack));
	}

	return 0;
}
