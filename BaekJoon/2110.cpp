#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    // N: # of houses, C: # of routers
    int N, C;
    cin >> N >> C;
    if ( !((2 <= N && N <= 200000) && (2 <= C && C <= N)) )
    {
        cout << "Not valid input.\n";
    }

    vector<int> input (N);
    for (int i = 0; i < N; i++)
    {
        cin >> input[i];
    }
    sort(input.begin(), input.end());
    
    vector<int> router_location;
    int count;
    int left_bound = 1, right_bound = input.back() - input.front();
    // The biggest gap between routers
    int gap = 0;
    do 
    {
        int mid = (right_bound + left_bound) / 2;
        
        router_location.clear();
        router_location.push_back(input[0]);
        count = 1;
        
        for (int i = 1; i < N; i++)
        {
            int loc = router_location.back() + mid;
            if (input[i] >= loc)
            {
                router_location.push_back(input[i]);
                count++;
            }
        }

        if (count < C)
        { 
            right_bound = mid - 1;
        }
        else
        {
            gap = mid;
            left_bound = mid + 1;
        }
    } while (left_bound <= right_bound);

    cout << gap << "\n";

    return 0;
}
