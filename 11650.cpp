// Using priority queue with std::greater

#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int main(void)
{
    int N;
    cin >> N;
    if (!(1 <= N && N <= 100000))
    {
        cout << "Not valid N\n";
    }
    int x, y;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
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