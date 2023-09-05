#include <stdio.h>

#include "Deque.h"

int main(void)
{
	Deque deq;
	// Create Deque and initialization
	DequeInit(&deq);

	// Save data
	DQAddFirst(&deq, 1);
	DQAddFirst(&deq, 2);
	DQAddFirst(&deq, 3);
	DQAddFirst(&deq, 4);
	DQAddFirst(&deq, 5);
	DQAddFirst(&deq, 6);


	// Remove data
	while (!DQIsEmpty(&deq))
	{
		printf("%d ", DQRemoveFirst(&deq));
	}

	printf("\n");

	// Save data
	DQAddLast(&deq, 1);
	DQAddLast(&deq, 2);
	DQAddLast(&deq, 3);
	DQAddLast(&deq, 4);
	DQAddLast(&deq, 5);
	DQAddLast(&deq, 6);

	while(!DQIsEmpty(&deq))
	{
		printf("%d ", DQRemoveLast(&deq));
	}

	return 0;
}
