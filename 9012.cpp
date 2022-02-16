#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void)
{
    // Num of test case
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++)
    {
        string input;
        cin >> input;
        int sSize = input.size();
        if ( !(2 <= sSize && sSize <= 50) )
        {
            printf("Invalid paraenthisis string.\n");
            return -1;
        }
 
        stack<char> s;
        for (int j = 0; j < sSize; j++)
        {
            if (input[j] == '(')
            {
                s.push(input[j]);
            }
            else
            {
                if (s.empty())
                {
                    cout << "NO\n";
                    break;
                }
                else
                {
                    s.pop();
                }
            }
            if (j == sSize -1)
            {
                if (s.empty())
                {
                    cout << "YES\n";
                }
                else
                {
                    cout << "NO\n";
                }
            }
        }
    }

    return 0;
}

/*
// Wook's Code
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    for (int line = 0; line < N; line++) {
        string s;
        cin >> s;
        
        int stack = 0;
        
        for (char c : s) {
            switch (c) {
                case '(':
                    stack++;
                    break;
                case ')':
                    stack--;
                    break;
            }
            
            if (stack < 0)
                break;
        }
        
        if (stack)
            cout << "NO\n";
        else
            cout << "YES\n";
    }
    
    return 0;
}
*/