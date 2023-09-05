#include <stdio.h>

#include "ArrayList.h"

int main(void)
{
	// Create array, Initialize
	List list;
	int data;
	ListInit(&list);

	// Save 5 data
	LInsert(&list, 11);
	LInsert(&list, 11);
	LInsert(&list, 22);
	LInsert(&list, 22);
	LInsert(&list, 33);

	// Print all of saved data
	printf("Number of all data: %d\n", LCount(&list);
	
	// Find first data
	if (LFirst(&list, &data))
	{
		printf("%d ", data);
		
		// Find second to last data
		while (LNext("%d ", data)
			printf("%d ", data);
	}
	printf("\n\n");

	// Find number 22, Delete all
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

	// After Deletion, Print remaining data
	printf("Number of all data: %d\n", LCount(&list);

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
