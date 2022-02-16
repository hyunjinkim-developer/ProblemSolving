// Using cpp STL stack

#include <iostream>
#include <stack>
#include <stdio.h>
#include <string.h>

using namespace std;

void push(int num, stack<int> &s)
{
    s.push(num);
}

void pop(stack<int> &s)
{
    if (s.empty())
    {
        cout << "-1" << '\n';
    }
    else
    {
        cout << s.top() << '\n';
        s.pop();
    }
}

void size(stack<int> &s)
{
    cout << s.size() << '\n';
}

void empty(stack<int> &s)
{
    // stack is empty
    if (s.empty()) 
    {
        cout << "1" << '\n';
    }
    else
    {
        cout << "0" << '\n';
    }
}

void top(stack<int> &s)
{
    if (s.empty())
    {
        cout << "-1" << "\n";
    }
    else
    {
        cout << s.top() << endl;
    }
}

int main(void)
{
    // Get input
    int N; // no. of orders
    scanf("%d", &N);
    if ( !(1 <= N && N <= 10000) )
    {
        printf("Not available N\n");
        return -1;
    }

    char str_order[6];
    int num;
    stack<int> s;
    for (int i = 0; i < N; i++)
    {
        // get orders for stack
        scanf("%s", str_order);
        
        // push into stack
        if (!strcmp(str_order, "push"))
        {
            scanf("%d", &num);
            push(num, s);
        }
        // pop from stack
        else if (!strcmp(str_order, "pop"))
        {
            pop(s);
        }
        // get size of stack
        else if (!strcmp(str_order, "size"))
        {
            size(s);
        }
        // check whether empty
        else if (!strcmp(str_order, "empty"))
        {
            empty(s);
        }
        // print top of stack
        else if (!strcmp(str_order, "top"))
        {
            top(s);
        }
        // if it is not a valid order
        else
        {
            printf("Invalid order has been typed.\n");
            return -1;
        }
    }
}

/*
// Wook's Code
#include <iostream>
#include <deque>
#include <map>

using namespace std;

int main()
{
    deque<int> stack;
    map<string, int> cmdMap = {{"push", 0}, {"pop", 1}, {"size", 2}, {"empty", 3}, {"top", 4}};
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        string cmd;
        int num;
        cin >> cmd;
        switch (cmdMap[cmd]) {
            case 0:
                cin >> num;
                stack.push_back(num);
                break;
                
            case 1:
                if (stack.empty())
                    cout << -1 << '\n';
                else {
                    cout << stack.back() << '\n';
                    stack.pop_back();
                }
                break;
                
            case 2:
                cout << stack.size() << '\n';
                break;
                
            case 3:
                cout << stack.empty() << '\n';
                break;
                
            case 4:
                if (stack.empty())
                    cout << -1 << '\n';
                else
                    cout << stack.back() << '\n';
                break;
        }
    }

    return 0;
}
*/