#include <iostream>
#include <list>

using namespace std;

// This class represents a undirected graph
// using adjacency list representation
class Graph
{
    int V; // # of vertices

    // Pointer to an array containing adjacency lists
    list<int> *adj;

    // Vistied vertices for DFS
    bool *dfsvisited;

public:
    Graph(int V); // Constructor

    // Function to add an edges to graph
    void addEdge(int v, int w);

    // Sort adjacent list
    void sortAdj();

    // Print edge
    void printEdge();

    // Print BFS traversal from a given source s
    void BFS(int s);

    // Print DFS traversal from a given source s
    void DFS(int v);
};

Graph::Graph(int V)
{
    this -> V = V;
    adj = new list<int>[V+1];
    dfsvisited = new bool[V+1];
}

void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w);
    adj[w].push_back(v);
}

void Graph::sortAdj()
{
    for (int vertex = 1; vertex <= V; vertex++)
    {
        adj[vertex].sort();
    }
}

void Graph::printEdge()
{
    list<int>::iterator i;
    for (int j = 1; j <= V; j++)
    {
        cout << j << ": ";
        for (i = adj[j].begin(); i != adj[j].end(); i++)
        {
            cout << *i << " ";
        }
        cout << endl;
    }
}

void Graph::BFS(int startV)
{
    // Mark all the vertices as not visited
    bool *visited = new bool[V + 1];
    for (int i = 1; i <= V; i++)
    {
        visited[i] = false;
    }

    // Create a queue for BFS
    list<int> queue;

    // Mark the current node as visited and enqueue it.
    visited[startV] = true;
    queue.push_back(startV);

    // iterator 'i' will be used to get 
    // all adjacent vertices of a vertex
    list<int>::iterator i;

    while (!queue.empty())
    {
        // Dequeue a vertex from queue and print it
        int currentV = queue.front();
        cout << currentV << " ";
        queue.pop_front();

        // Get all adjacent vertices of the dequeued vertex currentV.
        // If a adjacent has not been visited, 
        // then mark it visited and enqueue it
        for (i = adj[currentV].begin(); i != adj[currentV].end(); i++)
        {
            int adjVertex = *i;
            if (visited[adjVertex] == false)
            {
                visited[adjVertex] = true;
                queue.push_back(adjVertex);
            }
        }
    }
}

void Graph::DFS(int v)
{
    // Mark the current node as visited
    // and print it
    dfsvisited[v] = true;
    cout << v << " ";

    // Recur for all the vertices
    // adjacent to this vertex
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); i++)
    {
        int adjVertex = *i;
        if (dfsvisited[adjVertex] == false)
        {
            DFS(adjVertex);
        }
    }
}

int main(void)
{
    // input
    // N: # of vertices, M: # of edges, V: starting vertex
    int N, M, V;
    do
    {
        scanf("%d %d %d", &N, &M, &V);
    } while(!(1 <= N && N <= 1000) || !(1 <= M && M <= 10000) || !(1 <= V && V <= N));
    Graph g(N);

    // get edges
    int v, w;
    for (int i = 0; i < M; i++)
    {
        scanf("%d %d", &v, &w);
        g.addEdge(v, w);
    }
    g.sortAdj();
    // g.printEdge();

    g.DFS(V);
    cout << endl;
    g.BFS(V);
}