#include <iostream>
#include <vector>

#define fastio cin.sync_with_stdio(false); cin.tie(NULL);

using namespace std;

int filling(vector<int> &filled, int n)
{
    if (n == 1)
    {
        return filled[1] = 1;
    }
    if (n == 2)
    {
        return filled[2] = 3;
    }
    if (filled[n] != 0)
    {
        return filled[n];
    }
    else 
        return filled[n] = (filling(filled, n - 1) + filling(filled, n - 2) * 2) % 10007;
}

int main(void)
{
    fastio;

    int n;
    cin >> n;
    if (!(1 <= n && n <= 1000))
    {
        cout << "Not valid n.\n";
        return -1;
    }
    
    vector<int> filled(n + 1, 0);
    filling(filled, n);

    cout << filled[n];

    return 0;
}