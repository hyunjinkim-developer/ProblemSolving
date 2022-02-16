#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    string input;
    int input_size, input_count = 0;
    int small, cap, number, space;
   
    while (getline(cin, input))
    {
        small = 0, cap = 0, number = 0, space = 0;
        input_count++;
        input_size = input.size();
        if (!(1 <= input_size && input_size <= 100))
        {
            cout << "Not valid input.\n";
        }

        for (int i = 0; i < input_size; i++)
        {
            if ('a' <= input[i] && input[i] <= 'z')
            {
                small++;
            }
            else if ('A' <= input[i] && input[i] <= 'Z')
            {
                cap++;
            }
            else if ('0' <= input[i] && input[i] <= '9')
            {
                number++;
            }
            else if (input[i] == ' ')
            {
                space++;
            }
        }
        cout << small << " " << cap << " " << number << " " << space << "\n";
    }
    if (!(1 <= input_size && input_size <= 100))
    {
        cout << "Not valid input. The number of strings exceed 100.\n";
    }

    return 0;
}