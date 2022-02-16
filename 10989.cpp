// Using counting sort
// Using data structure vector, array with std::sort does not meet memory limitation
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

// Counting sort using map
void counting_sort_map(short int *input, const int *N)
{
    map<short int, short int> counting;
    
    for (int i = 0; i < *N; i++)
    {
        short int num = input[i];
        if (counting.count(num))
        {
            counting[num]++;
        }
        else
        {
            counting.insert({num, 1});
        }
    }

    map<short int, short int>::iterator iter = counting.begin();
    int idx = 0;
    while(iter != counting.end())
    {
        for(int i = 0; i < iter->second; i++)
        {
            input[idx++] = iter->first;
        }
        iter++;
    }
}

// Counting sort using array
void counting_sort_array(short int *input, const int *N)
{
    // all numbers are natural numbers 
    // with condition of less than or equal to 10000
    int counting[10001] = {0}; 
    for (int i = 0; i < *N; i++)
    {
        counting[input[i]]++;
    }
    int idx = 0;
    for (int i = 1; i < 10001; i++)
    {
        while (counting[i] != 0)
        {
            input[idx++] = i;
            counting[i]--;
        }
    }
}

int main(void)
{
    int N;
    cin >> N;
    if (!(1 <= N && N <= 10000000))
    {
        cout << "Not valid N.\n";
        return -1;
    }
    
    short int *numbers = new short int[N];
    for (int i = 0; i < N; i++)
    {  
        cin >> numbers[i];
        if (!(1 <= numbers[i] && numbers[i] <= 10000))
        {
            cout << "Not valid number\n";
            return -1;
        }
    }

    // counting_sort_map(numbers, &N);
    counting_sort_array(numbers, &N);

    for (short int* iter = numbers; iter != numbers + N; iter++)
    {
        cout << *iter << '\n';
    }

    delete[] numbers; 
    return 0;
}