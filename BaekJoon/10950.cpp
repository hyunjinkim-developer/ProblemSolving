#include <iostream>

using namespace std;
int main(void)
{
    int T;
    int A, B;

    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        do
        {
            scanf("%d %d", &A, &B);
        } while (!(A > 0) || !(B < 10)); 
        printf("%d\n", A + B);
    }
    return 0;
}