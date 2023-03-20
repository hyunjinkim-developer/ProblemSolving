#include <iostream>
#include <list>

using namespace std;

void printAdj(list<int> *adj, int N)
{
    cout << "Adj: " << endl;
    for (int i = 1; i <= N; i++)
    {
        cout << i << ": ";
        for (auto iter: adj[i])
        {
            cout << iter << " ";
        }
        cout << endl;
    }
}

void printVisited(bool *visited, int N)
{
    cout << "visited: " << endl;
    for (int i = 1; i <= N; i++)
    {
        cout << visited[i] << " ";
    }
    cout << endl;
}

int countVisited(bool *visited, int N)
{
    int count = 0;
    for (int i = 1; i <= N; i++)
    {
        if (visited[i] == true)
        {
            count++;
        }
    }
    return count;
}

int startV(bool *visited, int N)
{
    int startV;
    for (int i = 1; i <= N; i++)
    {
        if (visited[i] == false)
        {
            startV = i;
            break;
        }
    }

    return startV;
}

void DFS(list<int> *adj, bool *visited, int v)
{
    visited[v] = true;
    // // debug
    // cout << v << ' ';

    for(auto iter : adj[v])
    {
        if (visited[iter] == false)
        {
            DFS(adj, visited, iter);
        }
    }
}

int search(list<int> *adj, bool *visited, int N)
{
    int numCycle = 0;

    while (!(countVisited(visited, N) == N))
    {
        DFS(adj, visited, startV(visited, N));
        // // debug
        // cout << endl;
        numCycle++;
    }

    return numCycle;
}

int main(void)
{
    int T, N; // T: # of test case, N: # of permutation
    list<int> *adj; // Pointer to array pointing adjacency list 
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        do
        {
            scanf("%d", &N);
        } while (!(2 <= N && N <= 1000));

        adj = new list<int>[N+1];

        // Get directed edges
        for (int j = 1; j <= N; j++)
        {
            int v;
            scanf("%d", &v);
            adj[j].push_back(v);
        }

        bool *visited = new bool[N+1]; // Visited vertices for DFS
        // Initialize visited array as false
        for (int i = 1; i <= N; i++)
        {
            visited[i] = false;
        }
        // Make visited[0] not affected to DFS search process
        visited[0] = true; 

        cout << search(adj, visited, N) << endl;

        adj -> clear();
        free(visited);
    }
}




/* // other's code

#include <iostream>
#include <vector>

using namespace std;

void permutationCycle() {
    // input 
    int N;
    cin >> N;
    vector<int> permutation(N);
    
    for (int p = 0; p < N; p++) {
        cin >> permutation[p];
        permutation[p]--;
    }
    
    // circulate 
    vector<bool> visited(N, false);
    int cycle = 0;
    
    for (int p = 0; p < N; p++) {
        int num = p;
        
        if (!visited[num])
            cycle++;
            
        while(!visited[num]) {
            visited[num] = true;
            num = permutation[num];
        }
    }
    
    // output 
    cout << cycle << '\n';
}

int main() {
    int T;
    cin >> T;
    
    for (int test = 0; test < T; test++)
        permutationCycle();
}
*/
