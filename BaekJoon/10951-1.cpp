//using cin
#include <iostream>

using namespace std;

int main(void)
{
    int A, B;

    while(!(cin >> A >> B).eof())
    {
        if (!(A > 0) || !(B < 10))
            continue;
        else
            printf("%d\n", A + B);
    }
    return 0;
}