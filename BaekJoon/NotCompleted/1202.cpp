#include <algorithm>
#include <iostream>
#include <list>
#include <vector>

using namespace std;

bool sort_by_second(pair<int, int> &a, pair<int, int> &b)
{
    return (a.second > b.second);
}

// bool descending(int a, int b)
// {
//     return a > b;
// }

int main(void)
{
    int N, K; // # of jewels, bags
    cin >> N >> K;
    if ( !((1 <= N && N<= 300000) && (1 <= K && K <= 300000)))
    {
        cout << "Not valid N, K\n";
        return -1;
    }
    int M, V; // weight and value of jewels
    vector<pair<int, int>> jewels;
    for (int i = 0; i < N; i++)
    {
        cin >> M >> V;
        if ( !((0 <= M && M <= 1000000) && (0 <= V && V <= 1000000)))
        {
            cout << "Not valid M, V\n";
            return -1;
        }
        jewels.push_back(pair<int, int>(M, V));
    }
    sort_heap(jewels.begin(), jewels.end(), sort_by_second);

    int C; // maximum weight that one bag can carry
    list<int> bags;
    for (int i = 0; i < K; i++)
    {
        cin >> C;
        if ( !(1 <= C && C <= 100000000))
        {
            cout << "Not valid C\n";
            return -1;
        }
        bags.push_back(C);
    }
    sort_heap(bags.begin(), bags.end()); // replacing greater() with descending is available

    // one bag can only carry one jam
    long long total_value = 0;
    list<int>::iterator iter;
    for (auto jam: jewels)
    {
        if (bags.empty() == true)
        {
            break;
        }

        iter = lower_bound(bags.begin(), bags.end(), jam.first);
        if (iter != bags.end())
        {
            total_value += jam.second;
            bags.erase(iter);
        }
    }

    cout << total_value;

    return 0;
}
