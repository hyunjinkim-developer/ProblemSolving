#include <stdio.h>
#include "ArrayList.h"

void ListInit(List *plist)
{
	(plist -> numOfData) = 0;
	(plist -> curPosition) = -1;
}

void LInsert(List *plist, LData data)
{
	if (plist -> numOfData >= LIST_LEN)
	{
		puts("Can not save data. Storage is full.\n");
		return ;
	}
	
	plist -> arr[plist -> numOfData] = data;
	(plist-> numOfData) += 1;
}

int LFirst(List *plist, LData *pdata)
{
	if (plist -> numOfData == 0)
	{
		return FALSE;
	}

	(plist -> curPosition) = 0;
	*pdata = plist -> arr[0];
	return TRUE;
}

int LNext(List *plist, LData *pdata)
{
	if (plist -> curPosition >= (plist -> numOfData)-1)
	{
		return FALSE;
	}

	(plist -> curPosition) += 1;
	*pdata = plist -> arr[plist -> curPosition];
	return TRUE;
}

LData Remove(List *plist)
{
	int rpos = plist -> curPosition;
	int num = plist -> numOfData;
	int i;
	LData rdata = plist -> arr[rpos];

	for (i = rpos; i < num - 1; i++) 
	{
		plist -> arr[i] = plist -> arr[i+1];
	}

	(plist -> numOfData)--;
	(plist -> curPosition)--;
	return rdata;
}

int Lcount(List *plist)
{
	return plist -> numOfData;
}
