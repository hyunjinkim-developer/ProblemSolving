#include <iostream>

using namespace std;

int main(void)
{
    string input;
    cin >> input;
    if (input.size() > 100)
    {
        printf("Typed word is too long.\n");
        return -1;
    }
    int alphabet[26] = {0};

    for (int i = 0; i < input.size(); i++)
    {
        int idx = input[i] - 'a';
        alphabet[idx]++;
    }

    for (int i = 0; i < 26; i++)
    {
        cout << alphabet[i] << ' ';
    }
    return 0;
}