// Not finished Using BFs

#include <iostream>
#include <vector>

using namespace std;

void BFS(int startV, vector<int> &adj, int &bfsret)

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


        printf("%d\n", n - ret);
    }   

    return 0;
}