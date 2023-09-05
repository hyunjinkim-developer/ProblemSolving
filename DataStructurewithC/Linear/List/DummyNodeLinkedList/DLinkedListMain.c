#include <stdio.h>

#include "DLinkedList.h"

int WhoIsPreceding(int d1, int d2)
{
	// In ascendging order
	// if you want descending order
	// use if (d1 > d2)
	if (d1 < d2)
		return 0; //d1 precedes d2
	else
		return 1;
}

int main(void)
{
	// Make new list, and Initalize it
	List list;
	int data;
	ListInit(&list);

	// Set sorting order
	SetSortRule(&list, WhoIsPreceding);

	// Save 5 different data
	LInsert(&list, 11);
	LInsert(&list, 11);
	LInsert(&list, 22);
	LInsert(&list, 22);
	LInsert(&list, 33);
	
	// Print all of saved data
	printf("Number of Current Data: %d\n", LCount(&list));

	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
		{
			printf("%d ", data);
		}
	}
	printf("\n\n");

	// Remove all of node whose data == 22
	if (LFirst(&list, &data))
	{
		if (data == 22)
		{
			LRemove(&list);
		}

		while (LNext(&list, &data))
		{
			if (data == 22)
			{
				LRemove(&list);
			}
		}
	}

	// Print all of data left after deletion
	printf("Number of Current Data: %d\n", LCount(&list));

	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
		{
			printf("%d ", data);
		}
	}
	printf("\n\n");

	return 0;
}
