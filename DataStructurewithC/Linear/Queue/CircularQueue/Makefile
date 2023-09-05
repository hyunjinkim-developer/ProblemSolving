CC = gcc
CFLAGS = -Wall
TARGET = CircularQueue
OBJS = CircularQueueMain.o CircularQueue.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

CircularQueue.o: CircularQueue.h CircularQueue.c 
	$(CC) $(CFLAGS) -c CircularQueue.c

CircularQueueMain.o: CircularQueue.h CircularQueueMain.c
	$(CC) $(CFLAGS) -c CircularQueueMain.c

clean:
	rm *.o $(TARGET)
