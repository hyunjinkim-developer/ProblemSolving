#include <stdio.h>

#include "DBLinkedList.h"

int main(void)
{
	// Create DouBle Linked List
	// Initialization
	List list;
	ListInit(&list);
	int data;

	// Save 8 data
	LInsert(&list, 1);
	LInsert(&list, 2);
	LInsert(&list, 3);
	LInsert(&list, 4);
	LInsert(&list, 5);
	LInsert(&list, 6);
	LInsert(&list, 7);
	LInsert(&list, 8);

	// Search data
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		// Search data following next nodes
		while (LNext(&list, &data))
		{
			printf("%d ", data);
		}

		while (LPrevious(&list, &data))
		{
			printf("%d ", data);
		}
			
		printf("\n");
	}

	return 0;
}
