#include <iostream>
#include <list>
#include <map>

using namespace std;

int main (void)
{
    pair<int, int> ele;
    list<pair<int, int>> maplist;

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            maplist.push_back(pair<int, int>(i, j));
        }
    }

    // for(auto& iter : maplist)
    // {
    //      cout << iter.first << iter.second << " ";
    // }

    for (list<pair<int, int>>::iterator iter = maplist.begin(); iter != maplist.end(); iter++)
    {
            cout << iter->first << iter->second << " ";
    }
}