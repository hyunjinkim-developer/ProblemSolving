// Using Heap with vector

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool comparison(const pair<int, int> &a, const pair<int, int> &b)
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

int main(void)
{
    int N;
    cin >> N;
    if (!(1 <= N && N <= 100000))
    {
        cout << "Not valid N\n";
    }
    int x, y;
    vector<pair<int, int>> minHeap;
    for (int i = 0; i < N; i++)
    {
        cin >> x >> y;
        minHeap.push_back(pair<int, int>(x, y));
    }
    make_heap(minHeap.begin(), minHeap.end(), comparison);

    pair<int, int> p;
    while (minHeap.empty() == false)
    {
        p = minHeap.front();
        cout << p.first << " " << p.second << "\n";
        pop_heap(minHeap.begin(), minHeap.end(), comparison);
        minHeap.pop_back();
    }
    return 0;
}
