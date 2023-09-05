// Adjust DFS function efficiently

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

void DFS(int startV, vector<int> &adj, vector<bool> &visited, vector<bool> &matched, int &dfsret, int &cycleNum)
{ 
    visited[startV] = true;
    cycleNum++;
// cout << endl;
// printBool(visited);
// printInt(adj);

    int V = adj[startV];
    dfsret = V;
// cout << "dfsret " << dfsret << endl;
    
    if (visited[V] == false && matched[V] == false)
    {
        DFS(V, adj, visited, matched, dfsret, cycleNum);
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
        // Visited vertices for DFS
        
        int ret = 0;

// cout << "n: " << n << endl;

        // Get edges
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &adj[i]);
            adj[i]--;
            if (i == adj[i])
            {
                matched[i] = true;
                ret++;
            }
        }
        
        int dfsret; // last student searched with DFS
        int cycleNum; // # of students that make cycle
        for (int i = 0; i < n; i++)
        {
            if (matched[i] == true)
                continue;
            
            vector<bool> visited(n, false);
        // # of students who do not have team
// cout << "i: " << i << " -> ";
            cycleNum = 0;
            DFS(i, adj, visited, matched, dfsret, cycleNum);
            
            // Cycle: a team has made
            if (i == dfsret)
            {
                for (int i = 0; i < n ; i++)
                {
                    if (visited[i] == true)
                    {
                        matched[i]  = true;
                    }
                }
// cout << "for: " << i  << " / " << cycleNum << endl;
                ret += cycleNum;
            }
            
        }
// cout << "return : ";
        printf("%d\n", n - ret);
    }
    

    return 0;
}
