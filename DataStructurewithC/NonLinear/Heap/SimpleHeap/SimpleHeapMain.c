#include <stdio.h>

#include "SimpleHeap.h"

int main(void)
{
	Heap heap;
	HeapInit(&heap);

/*	HInsert(&heap, 'A', 1);
	HInsert(&heap, 'B', 2);
	HInsert(&heap, 'C', 3);
	printf("%c \n", HDelete(&heap));

	HInsert(&heap, 'A', 1);
	HInsert(&heap, 'B', 2);
	HInsert(&heap, 'C', 3);
	printf("%c \n", HDelete(&heap));
*/

	HInsert(&heap, 'C', 3);
	HInsert(&heap, 'D', 4);
	HInsert(&heap, 'E', 5);
	printf("%c \n", HDelete(&heap));

	HInsert(&heap, 'A', 1);
	HInsert(&heap, 'B', 2);
	HInsert(&heap, 'F', 6);
	while (!HIsEmpty(&heap))
	{
		printf("%c \n", HDelete(&heap));
	}

	return 0;
}
