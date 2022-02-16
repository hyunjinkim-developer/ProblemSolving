#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    // input N, M, height of trees
    int N, M;
    cin >> N >> M;
    if ( !((1 <= N && N && 1000000) && (1 <= M && M <= 2000000000)))
    {
        cout << "Not valid Input" << "\n";
    }
    
    vector<int> trees(N);
    for (int i = 0; i < N; i++)
    {
        cin >> trees[i];
    }

    // binary search
    int max_cut = 0;
    long long take_home = 0;
    int left = 1;
    int right = *max_element(trees.begin(), trees.end());
    while (left <= right)
    {
        take_home = 0;
        int cut_length = (left + right) / 2;
        for (int i = 0; i < N; i++)
        {
            if (trees[i] > cut_length)
                take_home += trees[i] - cut_length;
        }

        if (take_home >= M)
        {   
            max_cut = cut_length > max_cut ? cut_length : max_cut;
            left = cut_length + 1;
        }
        else
        {
            right = cut_length - 1;
        }
    }
    
    cout << max_cut << '\n';
    return 0;
}

/* 
// Wook's code
#include <iostream>
#include <vector>

using namespace std;

int main () {
    // input //
    int tree_num, necessary_length;
    cin >> tree_num >> necessary_length;
    
    vector<int> trees(tree_num);
    int max_height = 0;
    
    for (int tree = 0; tree < tree_num; tree++) {
        cin >> trees[tree];
        max_height = max_height < trees[tree] ? trees[tree] : max_height;
    }
    
    // chop tree 
    int l_bound = 0, u_bound = max_height;	// lower bound, upper bound
    unsigned int mid_height;
    long long chopped_length = 0;
    
    while (l_bound <= u_bound) {
        mid_height = (l_bound + u_bound) / 2;
        
        chopped_length = 0;
        for (int tree = 0; tree < tree_num; tree++)
            chopped_length += trees[tree] > mid_height ? trees[tree] - mid_height : 0;
        
        if (chopped_length >= necessary_length)
            l_bound = mid_height + 1;
        else if (chopped_length < necessary_length)
            u_bound = mid_height - 1;
    }
    
    // mid 바로 오른쪽인 mid + 1 에서 탐색이 끝난다. 이를 보정하기 위해 mid--를 해줍니다.
    if (chopped_length < necessary_length)
        mid_height--;
        
    cout << mid_height;

    return 0;
}
*/