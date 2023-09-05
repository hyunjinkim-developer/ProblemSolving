CC = gcc
CFLAGS = -Wall
TARGET = BinaryTreeTraverse
OBJS = BinaryTree.o BinaryTreeTraverseMain.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

BinaryTree.o: BinaryTree.c BinaryTree.h
	$(CC) $(CFLAGS) -c BinaryTree.c

BinaryTreeTraverseMain.o: BinaryTreeTraverseMain.c BinaryTree.h
	$(CC) $(CFLAGS) -c BinaryTreeTraverseMain.c

clean:
	rm *.o $(TARGET)
