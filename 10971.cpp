/*
	Graph traversal with recursion
	using class of cpp
	https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
 */

#include <iostream>
#include <list>
#include <map>

using namespace std;

// Graph class represents a directed graph
// using adjacency list representation
class Graph {
public:
	int N;
	int **cost;
	map<int, bool> visited;
	map<int, list<int>> adj;

	// function to get cost as std input
	void GetCost(int N);
	void PrintEdge();

	// function to add an edge to graph
	void AddEdge(int v, int w);

	void DFS(int v);
	void SumCost(int sumofcost, int curcost, int mincost);
};

// Get cost of each move
void Graph::GetCost(int numofnodes)
{
	N = numofnodes;
	cost = new int *[N];
	for (int i = 0; i < N; i++)
	{
		cost[i] = new int[N];
	}

	int input;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> input;
			cost[i][j] = input;
			if (input != 0)
				AddEdge(i, j);
		}
	}

	// Debug
	PrintEdge();
}

// Add edge to each vertex
void Graph::AddEdge(int v, int w)
{
	adj[v].push_back(w);
}

// Print all vertex and its corresponding edges
void Graph::PrintEdge()
{
	for (int v = 0; v < N; v++)
	{
		cout << "vertex: " << v << endl;
		for (list<int>::iterator iter = adj[v].begin(); iter != adj[v].end(); iter++)
		{
			cout << *iter << " ";
		}
		cout << endl;
	}
}

void Graph::DFS(int v)
{
	// Mark the current node as visited and
	// calculate sum of cost
	// print it
	visited[v] = true;
	cout << v << " ";

	// Recur for all the vertices adjacent
	// to this vertex
	for (list<int>::iterator iter = adj[v].begin(); iter != adj[v].end(); ++iter)
		if (!visited[*iter])
			DFS(*iter);
}


int main(void)
{
	int N;
	cin >> N;

	Graph g;
	g.GetCost(N);
	
	// DFS
	cout << "Traversal: ";
	g.DFS(1);

	return 0;
}
