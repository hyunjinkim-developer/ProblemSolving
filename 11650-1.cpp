// Using priority queue with custom comparison function

#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

class comparison
{
 public:
    bool operator() (const pair<int, int> &a, const pair<int, int> &b) const
    {
        if (a.first == b.first)
        {
            return a.second > b.second;
        }
        else
        {
            return a.first > b.first;
        }
    }
};

int main(void)
{
    int N;
    cin >> N;
    if (!(1 <= N && N <= 100000))
    {
        cout << "Not valid N\n";
    }
    int x, y;
    priority_queue<pair<int, int>, vector<pair<int, int>>, comparison> minHeap;
    for (int i = 0; i < N; i++)
    {
        cin >> x >> y;
        minHeap.push(pair<int, int>(x, y));
    }
    
    pair<int, int> p;
    while (minHeap.empty() == false)
    {
        p = minHeap.top();
        cout << p.first << " " << p.second << "\n";
        minHeap.pop();
    }
    return 0;
}
