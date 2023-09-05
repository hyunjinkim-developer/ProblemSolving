#include <stdio.h>

#include "ListBaseQueue.h"

int main(void)
{
	// Create Queue, Initialize it
	Queue q;
	QueueInit(&q);

	// Save Data
	Enqueue(&q, 1);
	Enqueue(&q, 2);
	Enqueue(&q, 3);
	Enqueue(&q, 4);
	Enqueue(&q, 5);

	// Remove Data
	while (!QIsEmpty(&q))
	{
		printf("%d ", Dequeue(&q));
	}

	return 0;
}
