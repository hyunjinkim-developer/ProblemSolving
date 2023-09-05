#include <stdio.h>

#include "DBDLinkedList.h"

int main(void)
{
	List list;
	ListInit(&list);

	Data data;

	// Save 8 data
	LInsert(&list, 1);
	LInsert(&list, 2);
	LInsert(&list, 3);
	LInsert(&list, 4);
	LInsert(&list, 5);
	LInsert(&list, 6);
	LInsert(&list, 7);
	LInsert(&list, 8);

	// Search saved data
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
		{
			printf("%d ", data);
		}
		printf("\n");
	}

	// Delete data which is mulitple of 2
	if (LFirst(&list, &data))
	{
		if ((data % 2) == 0)
		{
			LRemove(&list);
		}

		while (LNext(&list, &data))
		{
			if ((data % 2) == 0)
			{
				LRemove(&list);
			}
		}
	}

	// Search saved data
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
		{
			printf("%d ", data);
		}
		printf("\n");
	}
	
	return 0;
}
