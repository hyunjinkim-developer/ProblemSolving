CC = gcc
CFLAGS = -Wall
TARGET = BinaryTree
OBJS = BinaryTree.o BinaryTreeMain.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

BinaryTree.o: BinaryTree.c BinaryTree.h
	$(CC) $(CFLAGS) -c BinaryTree.c

BinaryTreeMain.o: BinaryTreeMain.c BinaryTree.h
	$(CC) $(CFLAGS) -c BinaryTreeMain.c

clean:
	rm *.o $(TARGET)
