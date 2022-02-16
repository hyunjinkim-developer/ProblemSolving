// Using contiguous data structure: vector/ array
// pros) random access
// cons) insertion, deletion
// Internal details of std::sort() is introsort

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    int N;
    cin >> N;
    if (!(1 <= N && N <= 1000000))
    {
        cout << "Not valid N.\n";
    }

    vector<int> vec;
    int element;
    for (int i = 0; i < N; i++)
    {
        cin >> element;
        vec.push_back(element);
    }
    sort(vec.begin(), vec.end());
    for (auto ele: vec)
    {
        cout << ele << '\n';
    }
    
    return 0;
}