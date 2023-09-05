CC = gcc
CFLAGS = -Wall
TARGET = BinaryTree2
OBJS = BinaryTree2.o BinaryTreeMain2.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

BinaryTree2.o: BinaryTree2.c BinaryTree.h
	$(CC) $(CFLAGS) -c BinaryTree2.c

BinaryTreeMain2.o: BinaryTreeMain2.c BinaryTree.h
	$(CC) $(CFLAGS) -c BinaryTreeMain2.c

clean:
	rm *.o $(TARGET)
