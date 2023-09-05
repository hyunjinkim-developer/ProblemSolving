#include <stdio.h>
#include <stdlib.h>

#include "ArrayList.h"
#include "Point.h"

int main(void)
{
	List list;
	Point compPos;
	Point *ppos;
	
	ListInit(&list);

	// Store 4 data
	ppos = (Point*) malloc(sizeof(Point));
	SetPointPos(ppos, 2, 1);
	LInsert(&list, ppos);

	ppos = (Point*) malloc(sizeof(Point));
	SetPointPos(ppos, 2, 2);
	LInsert(&list, ppos);

	ppos = (Point*) malloc(sizeof(Point));
	SetPointPos(ppos, 3, 1);
	LInsert(&list, ppos);

	ppos = (Point*) malloc(sizeof(Point));
	SetPointPos(ppos, 3, 2);
	LInsert(&list, ppos);

	// Print stored data
	printf("Number of current data: %d\n", LCount(&list));

	if (LFirst(&list, &ppos))
	{
		ShowPointPos(ppos);

		while (LNext(&list, &ppos))
		{
			ShowPointPose(ppos);
		}
	}
	printf("\n");

	// Delete all data with xpos == 2
	comPos.xpos = 2;
	comPos.ypos = 0;

	if (LFirst(&list, &ppos))
	{
		if (PointComp(ppos, &comPos) == 1)
		{
			ppos = LRemove(&list);
			free(ppos);
		}

		while (LNext(&list, &ppos))
		{
			if (PointComp(ppos, &comPos) == 1)
			{
				ppos = LRemove(&list);
				free(pos);
			}
		}
	}

	// Print all data left after deletion
	printf("Number of current data: %d\n", LCount(&list));

	if (LFirst(&list, &ppos))
	{
		ShowPointPos(ppos);

		while (LNext(&list, &ppos))
		{
			ShowPointPos(ppos);
		}
	}
	printf("\n");

	return 0;
}
