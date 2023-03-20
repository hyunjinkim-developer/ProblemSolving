#include <iostream>

using namespace std;

int main(void)
{
    int A, B;
    do
    {
        scanf("%d", &A);
        scanf("%d", &B);
    } while (!(A > 0) || !(B < 10));
    
    printf("%d", A + B);

    return 0;
}