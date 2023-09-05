CC = gcc
CFLAG = -Wall
TARGET = RateHambugerSim
OBJS = RateHambugerSim.o RateCircularQueue.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

RateHambugerSim.o: RateCircularQueue.h RateHambugerSim.c
	$(CC) $(CFLAGS) -c RateHambugerSim.c

RateCircularQueue.o: RateCircularQueue.h RateCircularQueue.c
	$(CC) $(CFLAGS) -c RateCircularQueue.c

clean:
	rm *.o $(TARGET)
