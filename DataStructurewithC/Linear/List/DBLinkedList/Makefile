CC = gcc
CFLAGS = -Wall
TARGET = DBLinkedList
OBJS = DBLinkedListMain.o DBLinkedList.o

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

DBLinkedList.o : DBLinkedList.h DBLinkedList.c
	$(CC) -c -o DBLinkedList.o DBLinkedList.c

DBLinkedListMain.o : DBLinkedList.h DBLinkedListMain.c
	$(CC) -c -o DBLinkedListMain.o DBLinkedListMain.c

clean:
	rm *.o $(TARGET)
