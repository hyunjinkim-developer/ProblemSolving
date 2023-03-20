// Do not save input seperately
// Apply counting sort as soon as input gets in
#include <algorithm>
#include <iostream>

using namespace std;

int main(void)
{
    // for faster input
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    if (!(1 <= N && N <= 10000000))
    {
        cout << "Not valid N.\n";
        return -1;
    }
    
    int numbers[10001] = {0};
    int num;
    for (int i = 0; i < N; i++)
    {  
        cin >> num;
        if (!(1 <= num && num <= 10000))
        {
            cout << "Not valid number\n";
            return -1;
        }
        numbers[num]++;
    }

    for (int i = 1; i <= 10000; i++)
    {
        while (numbers[i] != 0)
        {
            cout << i << '\n';
            numbers[i]--;
        }
    }

    return 0;
}