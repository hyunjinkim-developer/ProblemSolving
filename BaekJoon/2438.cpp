#include <iostream>

using namespace std;

int main(void)
{
    int input;
    scanf("%d", &input);
    
    for (int i = 1; i <= input; i++)
    {
        for (int j = 0; j < i; j++)
        {
            cout << "*";
        }
        printf("\n");
    }
}

