CC = gcc
CFLAG = -Wall
TARGET = HambugerSim
OBJS = HambugerSim.o CircularQueue.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

HambugerSim.o: CircularQueue.h HambugerSim.c
	$(CC) $(CFLAGS) -c HambugerSim.c

CircularQueue.o: CircularQueue.h CircularQueue.c
	$(CC) $(CFLAGS) -c CircularQueue.c

clean:
	rm *.o $(TARGET)
