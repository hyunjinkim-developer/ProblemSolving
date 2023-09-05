#include <stdio.h>

#include "CircularQueue.h"

int main(void)
{
	// Create Queue and Initialize it
	Queue q;
	QueueInit(&q);

	// Save data
	Enqueue(&q, 1);
	Enqueue(&q, 2);
	Enqueue(&q, 3);
	Enqueue(&q, 4);
	Enqueue(&q, 5);

	while (!QIsEmpty(&q))
	{
		printf("%d ", Dequeue(&q));
	}

	return 0;
}

