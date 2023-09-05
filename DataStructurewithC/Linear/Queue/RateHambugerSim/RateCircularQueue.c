#include <stdio.h>
#include <stdlib.h>

#include "RateCircularQueue.h"

void QueueInit(Queue *pq)
{
	pq -> front = 0;
	pq -> rear = 0;
}

int QIsEmpty(Queue *pq)
{
	if (pq -> front == pq -> rear)
	{
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}

int NextPosIdx(int pos)
{
	if (pos == QUE_LEN - 1)
	{
		return 0;
	}
	else
	{
		return pos + 1;
	}
}

int Enqueue(Queue *pq, Data data)
{
	if (NextPosIdx(pq -> rear) == pq -> front)
	{
		printf("Queue is full!\n");
		return -1;
	}

	pq -> rear = NextPosIdx(pq -> rear);
	pq -> queArr[pq -> rear] = data;
}

Data Dequeue(Queue *pq)
{
	if (QIsEmpty(pq))
	{
		printf("Queue is empty. Cannot dequeue any datum.\n");
		exit(-1);
	}

	pq -> front = NextPosIdx(pq -> front);
	return pq -> queArr[pq -> front];
}

Data QPeek(Queue *pq)
{
	if (QIsEmpty(pq))
	{
		printf("Queue is empty. Cannot peek any datum.\n");
		exit(-1);
	}

	return pq -> queArr[NextPosIdx(pq -> front)];
}
