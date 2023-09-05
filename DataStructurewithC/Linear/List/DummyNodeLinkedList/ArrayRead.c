#include <stdio.h>

int main(void)
{
	int arr[10];
	int readCount = 0;
	int readData;

	while (1)
	{
		printf("Type Natural Number: ");
		scanf("%d", &readData);

		if (readData < 1)
		{
			break;
		}
		else
		{
			arr[readCount] = readData;
			printf("arr: %d\n", arr[readCount]);
			readCount++;
		}
	}

	for (int i = 0; i < readCount; i++)
	{
		printf("%d", arr[i]);
	}

	return 0;
}
