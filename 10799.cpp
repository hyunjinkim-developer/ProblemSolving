#include <iostream>
#include <stack>
#include <vector>

using namespace std;

// count number of current sitck cut by laser
int countStick(int stickStart, int stickEnd, vector<float> cutLocation)
{
    int count = 0;
    for (auto ele : cutLocation)
    {
        if (stickStart <= ele && ele <= stickEnd)
        {
            count++;
        }
    }
    return count + 1;
}

int main(void)
{
    string input;
    cin >> input;

    stack<int> steelSticks;
    vector<float> cutLocation;
    int numStick = 0;
    for (int i = 0; i < input.size(); i++)
    {
        if (input[i] == '(')
        {
            steelSticks.push(i);
        }
        else // input[i] == ')'
        {
            int stickStart = steelSticks.top();
            steelSticks.pop();
            if (stickStart == i - 1)
            {
                // cutLocation.push_back((float)(stickStart + i) / 2);
                cutLocation.push_back(i); // 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다. 조건 입각 
            }
            else // End of current stick
            {
                numStick += countStick(stickStart, i, cutLocation);
            }
        }
    }

    printf("%d", numStick);
    
    return 0;
}

/*
// Wook's Code
#include <iostream>

using namespace std;

int main() {
    string input;
    cin >> input;
    
    int pipe_cnt = 0;
    int pipe_stack = 0;
    bool is_laser = false;
    
    for (char cmd : input) {
        if (cmd == '(') {
            pipe_stack++;
            is_laser = true;
        }
        
        else if (cmd == ')') {
            pipe_stack--;
            
            if (is_laser)
                pipe_cnt += pipe_stack;
            else
                pipe_cnt++;
            
            is_laser = false;
        }
    }
    
    cout << pipe_cnt;
    
    return 0;
}
*/