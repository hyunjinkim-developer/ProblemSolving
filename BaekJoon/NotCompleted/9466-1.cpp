// Using set for both visited and matched

#include <iostream>
#include <set>
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

void DFS(int startV, vector<int> &adj, set<int> &visited, int &dfsret)
{ 
    visited.insert(startV);
    // cout << endl;
    // printBool(visited);
    // printInt(adj);

    int V = adj.at(startV);
    dfsret = V;
    // cout << "dfsret " << dfsret << endl;
    
    if (visited.find(V) == visited.end())
    {
        DFS(V, adj, visited, dfsret);
    }
}

int main(void)
{
    // Get input
    int T; // #  of test case
    do 
    {
        scanf("%d", &T);
    } while (!(2 <= T && T <= 100000));

    for (int test = 0; test < T; test++)
    {
        int n; // # of students
        scanf("%d", &n);
        // Adjaceny list of directed graph
        vector<int> adj(n);
        // Students who are matched with teams
        set<int> matched;
        
        // Get edges
        int v;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &adj[i]);
            adj[i]--;
        }

        int dfsret = -1;
        for (int i = 0; i < n; i++)
        {
            if (matched.find(i) != matched.end())
                continue;

            // Visited vertices for DFS
            set<int> visited;
       
            DFS(i, adj, visited, dfsret);
            
            if (i == dfsret)
            {
                matched.insert(visited.begin(), visited.end());
            }
        }
        
        printf("%d\n", (int) n - matched.size());
    }
    

    return 0;
}
