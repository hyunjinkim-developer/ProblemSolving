#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "RateCircularQueue.h"

#define CUS_COME_TERM 15 

#define CHE_BUR 0
#define BUL_BUR 1
#define DUB_BUR 2

#define CHE_TERM 12
#define BUL_TERM 15
#define DUB_TERM 24

int main(void)
{
	int makeProc = 0;
	int cheOrder = 0, bulOrder = 0, dubOrder = 0;

	int trial = 100, ctrial = trial; // Trial for this simulation
	int exitCount = 0; // number of trial that has failed

	Queue que;

	QueueInit(&que);
	srand(time(NULL));

	while (ctrial != 0)
	{
		int flag = 0; 
		for (int sec = 0; sec < 3600; sec++)
		{
			// if program exited because of lack of memmotry flag == -1
			if (sec % CUS_COME_TERM == 0)
			{
				switch(rand() % 3)
				{
					case CHE_BUR:
						flag = Enqueue(&que, CHE_TERM);
						cheOrder++;
						break;

					case BUL_BUR:
						flag = Enqueue(&que, BUL_TERM);
						bulOrder++;
						break;

					case DUB_BUR:
						flag = Enqueue(&que, DUB_TERM);
						dubOrder++;
						break;
				}
			} 
			//printf("\nsec%d/ f %d\n", sec, flag);
			if (flag == -1)
			{
				exitCount++;
				printf("flag%d, 1\n", flag);
				printf("%d\n", ctrial);
				goto COUNT;
			}
				printf("flag%d, 2\n", flag);
	
			if (makeProc <=0 && !QIsEmpty(&que))
				makeProc = Dequeue(&que);

			makeProc--;
		}
				printf("flag%d, 3\n", flag);
		printf(" - Cheese buger: %d \n", cheOrder);
		printf(" - Bulgogi buger: %d \n", bulOrder);
		printf(" - Double buger: %d \n", dubOrder);
		printf(" - Waiting Romm Size: %d\n\n", QUE_LEN);

		COUNT: ;	

		ctrial--;
	}
	printf("Simulation Report! \n");
	printf("Total Trial: %d\n", trial);
	printf("Exited: %d\n", exitCount);
	printf("Executed: %.2f%%\n", (trial - exitCount) / (float) trial);

	return 0;
}
