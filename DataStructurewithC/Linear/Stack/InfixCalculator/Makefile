CC = gcc
CFLAG = -Wall
TARGET = InfixCalculator
OBJS = InfixCalculatorMain.o InfixCalculator.o InfixToPostfix.o PostCalculator.o ListBaseStack.o

$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

ListBaseStack.o: ListBaseStack.h ListBaseStack.c
	$(CC) -c ListBaseStack.c

InfixToPostfix.o: InfixToPostfix.h InfixToPostfix.c
	$(CC) -c InfixToPostfix.c
	
PostCalculator.o: PostCalculator.h PostCalculator.c 
	$(CC) -c PostCalculator.c 

InfixCalculator.o: InfixCalculator.h InfixCalculator.c
	$(CC) -c InfixCalculator.c

InfixCalculatorMain.o: InfixCalculatorMain.c
	$(CC) -c InfixCalculatorMain.c

clean:
	rm *.o $(TARGET)
