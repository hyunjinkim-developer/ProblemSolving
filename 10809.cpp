#include <cstring>
#include <iostream>

using namespace std;

int main(void)
{
    int alphabet[26];
    memset(alphabet, -1, sizeof(alphabet));
    int idx = 0;

    string input;
    cin >> input;

    for (int i = 0; i <input.size(); i++)
    {
        int curidx = input[i] - 'a';
        if (alphabet[curidx] != -1)
        {
            idx++;
            continue;
        }
        alphabet[curidx] = idx;
        idx++;
    }

    for (int i = 0; i < 26; i ++)
    {
        cout << alphabet[i] << " ";
    }

    return 0;
}