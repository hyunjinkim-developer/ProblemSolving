#include "UsefulHeap.h"

void HeapInit(Heap *ph, PrioirtyComp pc)
{
	ph -> numOfData;
	ph -> comp = pc;
}

int HisEmpty(Heap *ph)
{
	if (ph -> numOfData == 0)
	{
		return TRUE;
	}
	else
	{
		return FALSE;
	}
}

int GetParentIDX(int idx)
{
	return idx / 2;
}

int GetLChildIDX(int idx)
{
	return idx * 2;
}

int GetRChildIDX(int idx)
{
	return GetLChildIDX(idx) + 1;
}

int GetHiPriChildIDX(Heap *ph, int idx)
{
	if (GetLChildIDX(idx) > ph -> numOfData)
	{
		return 0;
	}
	else if (GetLChildIDX(idx) == ph -> numOfData)
	{
		return GetLChildIDX(idx);
	}
	else
	{
		if (ph  -> comp(ph -> heapArr[GetLChildIDX(idx)], 
					ph -> heapArr[GetRChildIDX(idx)]) <0)
		{
			return GetRChildIDX(idx);
		}
		else
		{
			return GetLChildIDX(idx);
		}

	}
}

void HInsert(Heap *ph, HData data)
{

}
