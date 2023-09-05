#ifndef __ARRAY_LIST_H__
#define __ARRAY_LIST_H__

#define TRUE 1 
#define FALSE 0

#define LIST_LEN 100
typedef int LData;

typedef struct __ArrayList
{
	LData arr[LIST_LEN]; // data
	int numOfData;	// number of data
	int curPosition; // position of data
} ArrayList;

typedef ArrayList List;

// Initialize
void ListInit(List *plist);
// Insert dat
void LInsert(List *plist, LData data);
	
// Find first data
int LFirst(List *plist, LData *pdata);
// Find second to last data
int LNext(List *plist, LData *pdata);
// Delete data
LData LRemove(List *plist);
// Count number of data
int LCount(List *plist);

#endif

