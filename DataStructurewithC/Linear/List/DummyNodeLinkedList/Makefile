CC	= gcc
CFLAGS = -Wall
LDFLAGS = 
OBJFILES = DLinkedList.o DLinkedListMain.o
TARGET = DLinkedList

all: $(TARGET)

$(TARGET): $(OBJFILES)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)

clean:
	rm -f $(OBJFILES) $(TARGET) *~
