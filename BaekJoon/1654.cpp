#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main (void)
{
    int K, N;
    cin >> K >> N;
    if ( !(1 <= 1 && K <= 10000) || !(1 <= K && K <= 1000000) || !(K <= N))
    {
        cout << "Not valid input.\n";
    }
    vector<unsigned int> input (K);
    for (int i = 0; i < K; i++)
    {
        cin >> input[i];
    }

    unsigned int right = *max_element(input.begin(), input.end());
    unsigned int left = 1;
    unsigned int max_length = 0;
    int count;

    while(left <= right)
    {
        count = 0;
        unsigned int mid = (left + right) / 2;

        for (int i = 0; i < K; i++)
        {
            count += (input[i] / mid);
        }

        if (count >= N)
        {
            left = mid + 1;
            max_length = mid > max_length ? mid : max_length;
        }
        else
        {
            right = mid - 1;
        }
    }

    cout << max_length << '\n';
    return 0;
}