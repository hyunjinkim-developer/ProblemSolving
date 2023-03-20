#include <iostream>

using namespace std;

// using scanf

int main(void)
{
    int A, B;

    while(scanf("%d %d", &A, &B) != -1) //  while(scanf("%d %d", &A, &B) == 2)
    {
        if (!(A > 0) || !(B < 10))
            continue;
        else
            printf("%d\n", A + B);
    }
    return 0;
}