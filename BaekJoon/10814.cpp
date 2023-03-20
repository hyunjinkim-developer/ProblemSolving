#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool cmp(const pair<int, string> &a, const pair<int, string> &b)
{
    return a.first < b.first;
}

int main(void)
{
    // Get N: # of members, ages and names of each memeber
    int N;
    cin >> N;
    if (!(1 <= N && N <= 100000))
    {
        cout << "Not valid N.\n";
        return -1;
    }
    int age;
    string name;
    int name_size;
    vector<pair<int, string>> members;
    for (int i = 0; i < N; i++)
    {
        cin >> age >> name;
        name_size = name.length();
        if (!(1 <= age && age <= 200) || !(name_size <= 100))
        {
            cout << "Not valid age and name length.\n";
            return -1;
        }
        for (int j = 0; j < name_size; j++)
        {
            if (isalpha(name[j]) == 0)
            {
                cout << "Name is not in alphabet.\n";
                return -1;
            }
        }
        members.push_back(pair<int, string>(age, name));
    }

    stable_sort(members.begin(), members.end(), cmp);

    for (auto e: members)
    {
        cout << e.first << ' ' << e.second << '\n';
    }

    return 0;
}