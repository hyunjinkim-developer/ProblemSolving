// A fast IO program
// Using ios::sync_with_stdio(false); and cin, cout

#include <iostream>
#include <vector>

using namespace std;

// void printBool(vector<bool> & vec)
// {
//     cout << "visited " ;
//     for (int i = 0; i < vec.size(); i++)
//     {
//         cout << vec.at(i) << " ";
//     }
//     cout << endl;
// }

// void printInt(vector<int> & vec)
// {
//     cout << "adj " ;
//     for (int i = 0; i < vec.size(); i++)
//     {
//         cout << vec.at(i) << " ";
//     }
//     cout << endl;
// }

void DFS(int startV, vector<int> &adj, vector<bool> &visited, int &dfsret)
{ 
    visited[startV] = true;
    // cout << endl;
    // printBool(visited);
    // printInt(adj);

    int V = adj[startV];
    dfsret = V;
    // cout << "dfsret " << dfsret << endl;
    
    if (visited[V] == false)
    {
        DFS(V, adj, visited, dfsret);
    }
}

int main(void)
{
    // A fast IO program
    ios::sync_with_stdio(false);

    // Get input
    int T; // #  of test case
    cin >> T;

    for (int test = 0; test < T; test++)
    {
        int n; // # of students
        do 
        {
            cin >> n;
        } while (!(2 <= n && n <= 100000));
        // Adjaceny list of directed graph
        vector<int> adj(n);
        // Students who are matched with teams
        vector<bool> matched(n, false);

        // Get edges
        for (int i = 0; i < n; i++)
        {
            cin >> adj[i];
            adj[i]--;
        }

        int ret = 0; // # of students who do not have team
        int dfsret; // last student searched with DFS
        for (int i = 0; i < n; i++)
        {
            if (matched[i] == true)
                continue;
            
            // Visited vertices for DFS
            vector<bool> visited(n, false);

            DFS(i, adj, visited, dfsret);
            
            // Cycle: a team has made
            if (i == dfsret)
            {
                for (int idx = 0; idx < n; idx++)   
                {
                    if (visited[idx] == true && matched[idx] == false)
                    {
                        matched[idx] = true;
                        ret++;
                    }
                }
            }
        }
        cout << n - ret << "\n";
    }

    return 0;
}
