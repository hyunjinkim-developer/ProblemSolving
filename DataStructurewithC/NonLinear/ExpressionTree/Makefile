CC = gcc
CFLAGS = -Wall
TARGET = ExpressionTree
OBJS = ExpressionMain.o ExpressionTree.o BinaryTree2.o ListBaseStack.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

ExpressionTree.o: ExpressionTree.c ListBaseStack.h BinaryTree2.h
	$(CC) $(CFLAGS) -c ExpressionTree.c

BinaryTree2.o: BinaryTree2.c BinaryTree2.h
	$(CC) $(CFLAGS) -c BinaryTree2.c

ListBaseStack.o: ListBaseStack.c ListBaseStack.h
	$(CC) $(CFLAGS) -c ListBaseStack.c

ExpressionMain.o: ExpressionMain.c ExpressionTree.h
	$(CC) $(CFLAGS) -c ExpressionMain.c


clean:
	rm *.o $(TARGET)
