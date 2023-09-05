CC = gcc
CFLAGS = -Wall
TARGET = ListBaseStack
OBJS = ListBaseStackMain.o ListBaseStack.o

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

ListBaseStack.o: ListBaseStack.h ListBaseStack.c
	$(CC) -c ListBaseStack.c

ListBaseStackMain.o: ListBaseStack.h ListBaseStackMain.c
	$(CC) -c ListBaseStackMain.c
	
clean :
	rm *.o $(TARGET)
