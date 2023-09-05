CC = gcc
CFLAGS = -Wall
TARGET = SimpleHeap
OBJS = SimpleHeap.o SimpleHeapMain.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

SimpleHeap.o: SimpleHeap.h SimpleHeap.c
	$(CC) $(CFLAGS) -c SimpleHeap.c

SimpleHeapMain.o: SimpleHeap.h SimpleHeapMain.c
	$(CC) $(CFLAGS) -c SimpleHeapMain.c

clean:
	rm *.o $(TARGET)
