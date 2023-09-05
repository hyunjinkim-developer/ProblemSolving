#include <stdio.h>
#include <stdlib.h>

#include "CLinkedList.h"

void ListInit(List *plist)
{
	plist -> tail = NULL;
	plist -> cur = NULL;
	plist -> before = NULL;
	plist -> numOfData = 0;
}

void LInsertFront(List *plist, Data data)
{
	Node *newNode = (Node *) malloc(sizeof(Node));
	newNode -> data = data;

	if (plist -> tail == NULL)
	{
		newNode -> next = newNode;
		plist -> tail = newNode;
	}
	else
	{
		newNode -> next = plist -> tail -> next;
		plist -> tail -> next = newNode;
	}

	(plist -> numOfData)++;
}

void LInsert(List *plist, Data data)
{
	Node *newNode = (Node *) malloc(sizeof(Node));
	newNode -> data = data;

	if (plist -> tail == NULL)
	{
		newNode -> next = newNode;
		plist -> tail = newNode;
	}	
	else
	{
		newNode -> next = plist -> tail -> next; 
		plist -> tail -> next = newNode;
		plist -> tail = newNode;
	}

	(plist -> numOfData)++;
}

int LFirst(List *plist, Data *pdata)
{
	// There is no data
	if (plist -> tail == NULL)
		return FALSE;

	plist -> before = plist -> tail;
	plist -> cur = plist -> tail -> next;

	*pdata = plist -> cur -> data;
	return TRUE;
}

int LNext(List *plist, Data *pdata)
{
	if (plist -> tail == NULL)
		return FALSE;

	plist -> before = plist -> cur;
	plist -> cur = plist -> cur -> next;

	*pdata = plist -> cur -> data;
	return TRUE;
}

Data LRemove(List *plist)
{
	Node * rpos = plist -> cur;
	Data rdata = rpos -> data;

	if (rpos == plist -> tail)
	{
		// There is only node left, which is going to be deleted
		if (plist -> tail -> next == plist -> tail)
			plist -> tail = NULL;
		// The node that you are trying to remove is tail of the list
		else
			plist -> tail = plist -> before;
	}

		plist -> before -> next = plist -> cur -> next;
		plist -> cur = plist -> before;
	
		free(rpos);
		(plist -> numOfData)--;
		return rdata;
}

int LCount(List *plist)
{
	return plist -> numOfData;
}
