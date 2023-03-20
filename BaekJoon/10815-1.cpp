// Using Binary Search
#include <algorithm>
#include <ctime>
#include <iostream>
#include <vector>

using namespace std;

int search_vector(vector<int> cards, int num)
{
    int left_bound = 0, right_bound = cards.size() - 1;
    do 
    {
        int mid = (left_bound + right_bound) / 2;

        //if (num == cards[left_bound] || num == cards[right_bound] || num == cards[mid])
        if (num == cards[mid])
        {
            return 1;
        }
        else if (num > cards[mid])
        {
            left_bound = mid + 1;
        }
        else
        {
            right_bound = mid - 1;
        }
    } while (left_bound <= right_bound);
    return 0;
}

int main(void)
{
    std::ios::sync_with_stdio(false); 
    cin.tie(NULL);
    time_t start, finish;
    start = time(NULL);

    int N, M;
    cin >> N;
    // cards that SG already have
    if (!(1 <= N && N <= 500000))
    {
        cout << "Not valid number of cards.\n";
    }
    vector<int> cards(N);
    for (int i = 0; i < N; i++)
    {
        cin >> cards[i];
    }

    // cards to search
    cin >> M;
    if (!(1 <= M && M <= 500000))
    {
        cout << "Not valid number of cards that will be searched.\n";
    }
    vector<int> search(M);
    for (int i = 0; i < M; i++)
    {
        cin >> search[i];
    }

    // find numbers in vector search from vector cards
    sort(cards.begin(), cards.end());
    
    for (int i = 0; i < M; i++)
    {
        cout << search_vector(cards, search[i]) << " ";
    }

    finish = time(NULL);
    cout << "\ntime: " << (double) finish - start << '\n';

    return 0;
}