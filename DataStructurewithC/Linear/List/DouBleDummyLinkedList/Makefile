CC = gcc
CFLAGS = -Wall
TARGET = DBDLinkedList
OBJS = DBDLinkedListMain.o DBDLinkedList.o

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

DBDLinkedList.o : DBDLinkedList.h DBDLinkedList.c
	$(CC) -c -o DBDLinkedList.o DBDLinkedList.c

DBDLinkedListMain.o : DBDLinkedList.h DBDLinkedListMain.c
	$(CC) -c -o DBDLinkedListMain.o DBDLinkedListMain.c

clean :
	rm *.o $(TARGET)
