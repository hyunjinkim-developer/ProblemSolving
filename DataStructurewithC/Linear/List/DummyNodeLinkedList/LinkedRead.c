#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
	int data;
	struct _node *next;
} Node;

int main(void)
{
	Node *head = NULL;
	Node *tail = NULL;
	Node *cur = NULL; // node pointer for searching data

	Node *newNode = NULL;
	int readData;

	// Save new data
	while(1)
	{
		printf("Input Natural Number: ");
		scanf("%d", &readData);
		if (readData < 1)
		{
			break;
		}

		// Insert new node
		newNode = (Node *) malloc(sizeof(Node));
		newNode -> data = readData;
		newNode -> next = NULL;

		if (head == NULL)
			head = newNode;
		else
			tail -> next = newNode;

		tail = newNode;
	}
	printf("\n");

	// Print saved data
	printf("Print all of saved data! \n");
	if (head == NULL)
	{
		printf("There is no saved natural number. \n");
	}
	else
	{
		cur = head;
		// Print first data
		printf("%d ", cur -> data);

		// Print second to last data
		while (cur -> next != NULL)
		{
			cur = cur -> next;
			printf("%d ", cur -> data);
		}
	}
	printf("\n\n");

	// Free memory
	// If there is no memory to be freed
	if (head == NULL)
	{
		return 0;
	}
	else
	{
		Node *delNode = head;
		Node *delNextNode = head -> next;

		printf("Delete %d.\n", head -> data);
		free(delNode);

		// Delete second to last Node
		while (delNextNode != NULL)
		{
			delNode = delNextNode;
			delNextNode = delNode -> next;

			printf("Delete %d.\n", delNode -> data);
			free(delNode);
		}
	}

	return 0;
}
