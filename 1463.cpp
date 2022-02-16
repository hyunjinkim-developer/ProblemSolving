// Using recursive fuction

#include <iostream>

using namespace std;

int min_c = 1000001;

void check(int N, int c)
{
    if (min_c <= c)
    {
        return ;
    }
    if (N == 1)
    {
        min_c = c;
        return ;
    }

    c++;
    if (N % 3 == 0)
    {
        check(N / 3, c);
    }
    if (N % 2 == 0)
    {
        check(N / 2, c);
    }
    
    check(N - 1, c);
}

int main(void)
{
    int N;
    cin >> N;
    if (!(1 <= N && N <= 1000000))
    {
        cout << "Not valid input\n";
        return -1;
    }

    check(N, 0);

    cout << min_c;
    return 0;
}