CC = gcc
CFLAGS = -Wall
TARGET = ListBaseQueue 
OBJS = ListBaseQueue.o ListBaseQueueMain.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

ListBaseQueueMain.o: ListBaseQueue.h ListBaseQueueMain.c
	$(CC) $(CFLAGS) -c ListBaseQueueMain.c

ListBaseQueue.o: ListBaseQueue.h ListBaseQueue.c
	$(CC) $(CFLAGS) -c ListBaseQueue.c

