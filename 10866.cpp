#include <deque>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(void)
{
    int N;
    scanf("%d", &N);
    if (!(1 <= N && N <= 10000))
    {
        printf("The number of orders exceeds 10000.\n");
    }

    deque<int> q;
    map<string, int> orderList = {{"push_front", 0}, {"push_back", 1}, {"pop_front", 2}, {"pop_back", 3}, {"size", 4}, {"empty", 5}, {"front", 6}, {"back", 7}};

    for (int i = 0; i < N; i++)
    {
        char order[11];
        scanf("%s", order);

        switch(orderList[order])
        {
            int num;
            case 0:
                scanf("%d", &num);
                q.push_front(num);
                break;
            case 1:
                scanf("%d", &num);
                q.push_back(num);
                break;
            case 2:
                if (q.empty())
                {
                    printf("-1\n");
                }
                else
                {
                    printf("%d\n", q.front());
                    q.pop_front();
                }
                break;
            case 3:
                if (q.empty())
                {
                    printf("-1\n");
                }
                else
                {
                    printf("%d\n", q.back());
                    q.pop_back();
                }
                break;
            case 4:
                printf("%lu\n", q.size());
                break;
            case 5:
                if (q.empty())
                {
                    printf("1\n");
                }
                else
                {
                    printf("0\n");
                }
                break;
            case 6:
                if (q.empty())
                {
                    printf("-1\n");
                }
                else
                {
                    printf("%d\n", q.front());
                }   
                break;
            case 7:
                if (q.empty())
                {
                    printf("-1\n");
                }
                else
                {
                    printf("%d\n", q.back());
                }
                break;
            default:
                printf("Not valid order. Try again.\n");
                break;
        }
    }
    return 0;
}