#include <map>
#include <iostream>

using namespace std;

class Queue
{
    int que[100000];
    int firstIdx = 0;
    int lastIdx = 0;
    int next = 0;

public:
    // Push X into queue
    void push(int X);

    // Pop number in the front and Print it
    // If queue is empty, print -1
    void pop(void);

    // Print number of element in queue
    void size(void);

    // If the queue is empty, print 1
    // else print 0
    int empty(void);

    // Print the first element of queue
    // If the queue is empty, print -1
    void front(void);

    // Print the last element of queue
    // If the queue is empty print -1
    void back(void);

    // Print all the element in the queue with index
    void print(void);
};

void Queue::push(int X)
{
    lastIdx = next;
    que[lastIdx] = X;
    next++;
}

int Queue::empty(void)
{
    // The queue is empty.
    if (firstIdx == next)
    {
        return 1;
    }
    else 
    {
        return 0;
    }
}

void Queue::pop(void)
{
    if (this->empty() == 1)
    {
        printf("-1\n");
    }
    else
    {
        printf("%d\n", que[firstIdx]);
        firstIdx++;
    }
}

void Queue::size(void)
{
    if (firstIdx == next)
    {
        printf("0\n");
    }
    else
    {
        printf("%d\n", lastIdx - firstIdx + 1);
    }
}

void Queue::front(void)
{
    if (this->empty() == 1)
    {
        printf("-1\n");
    }
    else
    {
        printf("%d\n", que[firstIdx]);
    }
}

void Queue::back(void)
{
    if (this->empty() == 1)
    {
        printf("-1\n");
    }
    else
    {
        printf("%d\n", que[lastIdx]);
    }
}

// void Queue::print(void)
// {
//     for (int i = firstIdx; i <= lastIdx; i++)
//     {
//         printf("%d ", que[i]);
//     }
//     printf("\n");
// }

int main(void)
{
    int N;
    scanf("%d", &N);
    if (!(1 <= N && N <= 10000))
    {
        printf("The number of order is wrong.\n");
        return -1;
    }

    Queue que;
    map<string, int> orderList = {{"push", 0}, {"pop", 1}, {"size", 2}, {"empty", 3}, {"front", 4}, {"back", 5}};

    for (int round = 0; round < N; round++)
    {
        char order[6];
        // scanf("%s", order);
        cin >> order;
        switch(orderList[order])
        {
            case 0:
                int X;
                // scanf("%d", &X);
                cin >> X;
                que.push(X);
                break;

            case 1:
                que.pop();
                break;

            case 2:
                que.size();
                break;

            case 3:
                cout << que.empty() << '\n';
                break;

            case 4:
                que.front();
                break;

            case 5:
                que.back();
                break;

            default:
                printf("Not valid command. Try again.\n");
                break;
        }
    }

    return 0;
}