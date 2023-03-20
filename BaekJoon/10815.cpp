// Using map count()

#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

int main(void)
{
    /* IO for large files speed comparison
    Input:
    1) fread
    2) getchar
    3)
    std::ios::sync_with_stdio(false); 
    cin.tie(NULL);
    4) std::ios::sync_with_stdio(false); 
    5) scanf
    
    Output:
    // using '\n' is faster than using endl
    1)fwrite
    2) std::ios::sync_with_stdio(false); 
    3)
    std::ios::sync_with_stdio(false); 
    cout.tie(NULL);
    4) printf  
    */

    std::ios::sync_with_stdio(false); 
    cin.tie(NULL);

    int N, M;
    cin >> N;
    // cards that SG already have
    if (!(1 <= N && N <= 500000))
    {
        cout << "Not valid number of cards.\n";
        return -1;
    }
    map<int, int> cards;
    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        cards[num] = 1;
    }

    // search
    cin >> M;
    if (!(1 <= M && M <= 500000))
    {
        cout << "Not valid number of cards that will be searched.\n";
        return -1;
    }
    for (int i = 0; i < M; i++)
    {
        int num;
        cin >> num;
        cout << cards.count(num) << " ";
    }

    return 0;
}

/*
// Wook's code
#include <iostream>

using namespace std;

bool numbers[20000001] = {0};

int main()
{
    int N, M;
    int num;
    
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &num);
        numbers[num + 10000000] = 1;
    }
    
    scanf("%d", &M);
    for (int i = 0; i < M; i++) {
        scanf("%d", &num);
        cout << numbers[num + 10000000] << ' ';
    }

    return 0;
}
*/