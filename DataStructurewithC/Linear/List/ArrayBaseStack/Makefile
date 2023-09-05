CC = gcc
CFLAGS = -Wall
TARGET = ArrayBaseStack
OBJS = ArrayBaseStackMain.o ArrayBaseStack.o 

$(TARGET) : $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

ArrayBaseStackMain.o : ArrayBaseStack.h ArrayBaseStackMain.c
	$(CC) -c -o ArrayBaseStackMain.o ArrayBaseStackMain.c
	
ArrayBaseStack.o : ArrayBaseStack.h ArrayBaseStack.c
	$(CC) -c -o ArrayBaseStack.o ArrayBaseStack.c

clean :
	rm *.o $(TARGET)
