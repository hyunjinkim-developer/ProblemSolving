CC = gcc
CFLAGS = -Wall
TARGET = Deque
OBJS = DequeMain.o Deque.o

$(TARGET): $(OBJS)
	$(CC) $(CFLASG) -o $(TARGET) $(OBJS)

Deque.o: Deque.h Deque.c 
	$(CC) $(CFLAGS) -c Deque.c

DequeMain.o: Deque.h DequeMain.c
	$(CC) $(CLFAGS) -c DequeMain.c

clean:
	rm *.o $(TARGET)

