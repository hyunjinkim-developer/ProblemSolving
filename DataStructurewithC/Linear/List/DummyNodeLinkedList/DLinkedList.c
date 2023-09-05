#include <stdio.h>
#include <stdlib.h>

#include "DLinkedList.h"

void ListInit(List *plist)
{
	plist -> head = (Node *)malloc(sizeof(Node)); // Dummy Node
	plist -> head -> next = NULL;
	plist -> comp = NULL;
	plist -> numOfData = 0;
}

void FInsert(List *plist, LData data)
{
	Node *newNode = (Node *) malloc(sizeof(Node));
	newNode -> data = data;

	// newNode will point next node that  head node pointer pointed
	newNode -> next = plist -> head -> next; 
	plist -> head -> next = newNode;

	(plist -> numOfData)++;
}

void SInsert(List *plist, LData data)
{
	Node *newNode = (Node *)malloc(sizeof(Node));
	Node *pred = plist -> head; //pred point Dummy node
	newNode -> data = data;

	// Find location of new node
	while (pred -> next != NULL && plist -> comp(data, pred -> next -> data) != 0)
	{
		pred = pred -> next;
	}
	
	newNode -> next = pred -> next;
	pred -> next = newNode;

	(plist -> numOfData)++;
}

void LInsert(List *plist, LData data)
{
	if (plist -> comp == NULL)
	{
		FInsert(plist, data);
	}
	else
	{
		SInsert(plist, data);
	}
}

int LFirst(List *plist, LData *pdata)
{
	// There is no node
	// plist -> head point Dummy node
	if (plist -> head -> next == NULL)
	{
		return FALSE;
	}
	
	plist -> before = plist -> head;
	plist -> cur = plist -> head -> next;

	*pdata = plist -> cur -> data;
	return TRUE;
}

int LNext(List *plist, LData *pdata)
{
	// There is no more nodes
	if (plist -> cur -> next == NULL)
	{
		return FALSE;
	}
	
	plist -> before = plist -> cur;
	plist -> cur = plist -> cur -> next;

	*pdata = plist -> cur -> data;
	return TRUE;
}

LData LRemove(List *plist)
{
	Node *rpos = plist -> cur;
	LData rdata = plist -> cur -> data;

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

void SetSortRule(List *plist, int (*comp)(LData d1, LData d2))
{
	plist -> comp = comp;	
}
