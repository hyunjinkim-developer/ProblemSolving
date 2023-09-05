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
    visited.at(startV) = true;
    // cout << endl;
    // printBool(visited);
    // printInt(adj);

    int V = adj.at(startV);
    dfsret = V;
    // cout << "dfsret " << dfsret << endl;
    
    if (visited.at(V) == false)
    {
        DFS(V, adj, visited, dfsret);
    }
}

int main(void)
{
    // Get input
    int T; // #  of test case
    scanf("%d", &T);

    for (int test = 0; test < T; test++)
    {
        int n; // # of students
        do 
        {
            scanf("%d", &n);
        } while (!(2 <= n && n <= 100000));
        // Adjaceny list of directed graph
        vector<int> adj(n);
        // Students who are matched with teams
        vector<bool> matched(n, false);

        // Get edges
        int v;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &adj[i]);
            adj[i]--;
        }

        int ret = 0; // # of students who do not have team
        int dfsret;
        for (int i = 0; i < n; i++)
        {
            if (matched[i] == true)
                continue;

            // Visited vertices for DFS
            vector<bool> visited(n, false);

            DFS(i, adj, visited, dfsret);
            
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

        printf("%d\n", n - ret);
    }

    return 0;
}
