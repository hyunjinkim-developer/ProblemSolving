// Using Non contiguous data structure: list
// pros) insertion, deletion
// cons) random access
// list.sort()

#include <algorithm>
#include <iostream>
#include <list>

using namespace std;

int main(void)
{
    int N;
    cin >> N;
    if (!(1 <= N && N <= 1000000))
    {
        cout << "Not valid N.\n";
    }

    list<int> list;
    int element;
    for (int i = 0; i < N; i++)
    {
        cin >> element;
        list.push_back(element);
    }
    list.sort();
    for (auto ele: list)
    {
        cout << ele << '\n';
    }
    
    return 0;
}