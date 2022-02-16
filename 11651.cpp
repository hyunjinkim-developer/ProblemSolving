#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool comp(const pair<int, int> &a, const pair<int, int> &b)
{
    if (a.second != b.second)
        return a.second < b.second;
    else
        return a.first < b.first;
}

int main(void)
{
    // Get input: N, x, y
    int N;
    cin >> N;
    if (!(1 <= N && N <= 100000))
    {
        cout << "Not valid N.\n";
        return -1;
    }

    int x, y;
    vector<pair<int, int>> coordinate;
    for (int i = 0; i < N; i++)
    {
        cin >> x >> y;
        if (!(-100000 <= x && x <= 100000) || !(-100000 <= y && y <= 100000))
        {
            cout << "Not valid x or y.\n";
            return -1;
        }
        coordinate.push_back(pair<int, int>(x, y));
    }
    
    // Sort coordinates in ascending order of y 
    // if y is the same, in ascending order of x
    sort(coordinate.begin(), coordinate.end(), comp);

    for (auto element: coordinate)
    {
        cout << element.first << " " << element.second << "\n";
    }

    return 0;
}