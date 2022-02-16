#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    int n;
    cin >> n;
    if (!(1 <= n && n <= 1000))
    {
        cout << "Not valid n\n";
        return -1;
    }
    vector<unsigned int> result = {1, 2};
    for(int i = 2; i < n; i++)
    {
        result.push_back((result[i - 2] + result[i - 1]) % 10007);
    }

    unsigned int answer = result.back();
    if (n == 1 || n == 2)
    {
        answer = result[n - 1];
    }
    cout << answer;

    return 0;
}