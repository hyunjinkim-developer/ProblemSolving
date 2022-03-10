// std::getline (string)
// istream& getline (istream& is, string& str);

#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    string input;
    getline(cin, input);
    int N = input.length();
    int i = 0;
    while(i != N)
    {   
        cout << input[i];
        i++;
        if (i % 10 == 0)
            cout << '\n';
    }   
    return 0;
}
