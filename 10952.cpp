#include <iostream>

using namespace std;

int main(void)
{
    int A, B;
    while (true)
    {
        do
        {
            scanf("%d %d", &A, &B);
        
            if (A == 0 && B == 0)
            {
                return 0;
            }
        } while(!(0 < A) || !(B < 10));
        
        printf("%d\n", A + B);
    }
}