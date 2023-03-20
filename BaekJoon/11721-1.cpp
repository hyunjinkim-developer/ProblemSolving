// std::basic_istream
// basic_istream& getline( char_type* s, std::streamsize count );

#include <iostream>

using namespace std;

int main(void)
{
    char input[100];
    cin.getline(input, 100);
    int i = 0;
    while(input[i] != '\0')
    {   
        cout << input[i];
        i++;
        if (i % 10 == 0)
            cout << '\n';
    }   
    return 0;
}
