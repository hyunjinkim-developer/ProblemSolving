#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    if (!(1 <= N && N <= 1000000) || !(1 <= M && M <= 1000000))
    {
        cout << "Not valid N, M\n";
        return -1;
    }
    vector<int> A(N);
    vector<int> B(M);
    for (int idxA = 0; idxA < N; idxA++)
    {
        cin >> A[idxA];
    }
    for (int idxB = 0; idxB < M; idxB++)
    {
        cin >> B[idxB];
    }

    vector <int> result;
    int idxA = 0, idxB = 0;
    while (!(idxA == N && idxB == M))
    {
        if (idxA == N)
        {
            for (int i = idxB; i < M; i++)
            {
                result.push_back(B[i]);
            }
            break;
        }
        else if (idxB == M)
        {
            for (int i = idxA; i < N; i++)
            {
                result.push_back(A[i]);
            }    
            break;
        }
        else
        {
            if (A[idxA] > B[idxB])
            {
                result.push_back(B[idxB++]);
            }
            else 
            {
                result.push_back(A[idxA++]);
            }
        }
    }

    for (auto element: result)
    {
        cout << element << " ";
    }

    return 0;
}