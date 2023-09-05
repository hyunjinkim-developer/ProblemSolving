CC = gcc
CLFAGS = -Wall
TARGET = CLinkedList
OBJS = CLinkedList.o CLinkedListMain.o

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

CLinkedList.o : CLinkedList.h CLinkedList.c 	
	gcc -c -o CLinkedList.o CLinkedList.c

CLinkedListMain.o : CLinkedList.h CLinkedListMain.c
	gcc -c -o CLinkedListMain.o CLinkedListMain.c

clean :
	rm *.o CLinkedList
