#include <stdio.h>

#include "CLinkedList.h"

int main (void)
{
	// Create Circular Linked List
	//Initialization
	List list;
	ListInit(&list);
	int data;

	// Save 5 data in the list
	LInsert(&list, 3);
	LInsert(&list, 4);
	LInsert(&list, 5);
	LInsertFront(&list, 2);
	LInsertFront(&list, 1);
	
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		for(int i = 0; i < (LCount(&list) * 3) - 1; i++)
		{
			if (LNext(&list, &data))
			{
				printf("%d ", data);
			}
		}
	}
	printf("\n\n");

	int nodeNum = nodeNum = LCount(&list);
	
	// Remove all the data multiple of 2
	if (nodeNum != 0)
	{
		LFirst(&list, &data);
		if ((data % 2) == 0)
		{
			LRemove(&list);
		}

		for (int i = 0; i < nodeNum - 1; i++)
		{
			LNext(&list, &data);
			if ((data % 2) == 0)
			{
				LRemove(&list);
			}
		}
	}

	// Print all of saved data
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		nodeNum = LCount(&list);
		for (int i = 0; i < nodeNum - 1; i++)
		{
			if (LNext(&list, &data))
			{
				printf("%d ", data);
			}
		}
	}

	return 0;
}
