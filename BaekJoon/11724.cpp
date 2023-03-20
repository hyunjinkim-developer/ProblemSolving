#include <iostream>
#include <list>
#include <vector>

using namespace std;

void printEdge(list<int> *adj, int N)
{
    list<int>::iterator i;
    for(int vertex = 1; vertex <= N; vertex++)
    {
        cout << vertex << ": ";
        for (i = adj[vertex].begin(); i != adj[vertex].end(); i++)
        {
            cout << *i << " ";
        }
        cout << endl;
    }
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

int findNotVisited(bool *visited, int N)
{
    
    int nextVertex;
    for (int i = 1; i <= N; i++)
    {
        if (visited[i] == false)
        {
            nextVertex = i;
            break;
        }
    }
    return nextVertex;
}

int main(void)
{
    // N: # of vertices, M: # of edges
    int N, M;
    do
    {
        scanf("%d %d", &N, &M);
    } while (!(1 <= N && N <= 1000) || !(0 <= M && M <= N*(N-1)/2));
    list<int> *adj = new list<int>[N+1];
    // vector< list<int> > adj(N+1, list<int>());

    // Add Edges
    int u, v;
    for (int i = 0; i < M; i++)
    {
        do
        {
            scanf("%d %d", &u, &v);        
        } while (!(1 <= u <= N) || !(1 <= v <= N) || (u == v));
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // printEdge(adj, N);

    // Calculate # of Connected Component
    int CC = 0;

    // Mark all the vertices are not visited
    bool *visited = new bool[N+1];
    for (int i = 1; i <= N; i++)
    {
        visited[i] = false;
    }

    // Create a queue for BFS
    list<int> queue;

    // iterator 'i' will be used to get 
    // all adjacent vertices of a vertex
    list<int>::iterator i;
    
    while(countVisited(visited, N) != N)
    {
        int nextVertex = findNotVisited(visited, N);
        // cout << "nextVertex: " << nextVertex << endl;
        // Mark the current node as visited and enqueue it
        visited[nextVertex] = true;
        queue.push_back(nextVertex);

        while(!queue.empty())
        {
            // Dequeue a vertex from queue and print it
            int currentV = queue.front();
            // cout << currentV << " ";
            queue.pop_front();

            // Get all adjacent vertices of the dequeued vertex s.
            // If a adjacent has not been visited,
            // then mark it visited and endqueue it
            for (i = adj[currentV].begin(); i != adj[currentV].end(); i++)
            {
                int adjV = *i;
                if (visited[adjV] == false)
                {
                    visited[adjV] = true;
                    queue.push_back(adjV);
                }
            }
        }
        // cout << endl << "count: " << countVisited(visited, N) << endl;
        CC++;
    }
    
    // Print # of Connected Component
    cout << CC;
}

