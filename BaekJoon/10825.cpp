#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

bool cmp(const tuple<string, int, int, int> &a, const tuple<string, int, int, int> &b)
{
    if (get<1>(a) != get<1>(b))
    {
         return get<1>(a) > get<1>(b); // Korean scores in descending order
    }
    else // if Korean scores are the same
    {
        if(get<2>(a) != get<2>(b)) 
        {
            return get<2>(a) < get<2>(b); // English scores in ascending order
        }
        else // if Korean and English scores are the same
        {
            if (get<3>(a) != get<3>(b))
            {
                return get<3>(a) > get<3>(b); // Math scores in descending order
            }
            else // if Korean, English, Math scores are the same
            {
                return get<0>(a) < get<0>(b); // names in lexicographical order (Upper case comes first)
            }
        }
    }
}

int main(void)
{
    // Get input: N(# of classmates), each classmate's name, score of Korean, English, math
    int N; 
    cin >> N;
    if (!(1 <= N && N <= 100000))
    {
        cout << "Not valid number of classmates.\n";
        return -1;
    }
    
    vector<tuple<string, int, int, int>> mates(N);
    for (int i = 0; i < N; i++)
    {
        // get input in name, Korean, English, math order
        cin >> get<0>(mates[i]) >> get<1>(mates[i]) >> get<2>(mates[i]) >> get<3>(mates[i]);
        
        int name_length = get<0>(mates[i]).size();
        if (name_length > 10)
        {
            cout << "Not valid name length.\n";
            return -1;
        }
        if (!all_of(get<0>(mates[i]).cbegin(), get<0>(mates[i]).cend(), [](char c){ return isalpha(c); }))
        {
            cout << "Not valid name. This name has non-alphabet character.\n";
            return -1;
        }

        //? This with for loop
        int scoreK = get<1>(mates[i]);
        int scoreE = get<2>(mates[i]);
        int scoreM = get<3>(mates[i]);
        if ( !(1 <= scoreK && scoreK <= 100) || !(1 <= scoreE && scoreE <= 100) || !(1 <= scoreM && scoreM <= 100))
        {
            cout << "Not valid score.\n";
            return -1;
        }
        
    }

    // sort classmates based on rules.
    sort(mates.begin(), mates.end(), cmp);

    for (auto element: mates)
    {
        cout << get<0>(element) << '\n';
    }

    return 0;
}