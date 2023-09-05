// Using List for Visited

#include <algorithm>
#include <iostream>
#include <list>
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

void DFS(int startV, vector<int> &adj, list<int> &visited, int &dfsret)
{ 
    visited.push_back(startV);
    // cout << endl;
    // printBool(visited);
    // printInt(adj);

    int V = adj[startV];
    dfsret = V;
    // cout << "dfsret " << dfsret << endl;
    
    if (find(visited.begin(), visited.end(), V) == visited.end())
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
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &adj[i]);
            adj[i]--;
        }

        int ret = 0; // # of students who do not have team
        int dfsret; // last student searched with DFS
        for (int i = 0; i < n; i++)
        {
            if (matched[i] == true)
                continue;
            
            // Visited vertices for DFS
            list<int> visited;

            DFS(i, adj, visited, dfsret);
            
            // Cycle: a team has made
            if (i == dfsret)
            {
                for(auto ele: visited)
                {
                    matched[ele] = true;
                    ret++;
                }
            }
        }


        
        printf("%d\n", n - ret);
    }
    

    return 0;
}
