/*
	Graph traversal recursively
reference:
	https://githubseob.tistory.com/m/90
*/

#include <iostream>
#include <vector>

using namespace std;

int N;
vector<vector<int>> input;
// maximum: cost * cities  = 10^6 * (10 * 10) 
int answer = 1e9;


void Move(int start, int node, int cost, vector<bool> visited)
{
	// cost == 0 means Move function just started
	if (cost != 0)
		visited[node] = true;
	
	int visit_count = 0;

	for (int idx = 0; idx < N; idx++)
	{
		int next_cost = cost + input[node][idx];
		if(visited[idx]) // visited[idx] != false
			visit_count++;
		// Next possible node is not visited
		// next move possible cost is smaller than current smallest traversal cost
		// next possible node is available
		else if (!visited[idx] && next_cost < answer && input[node][idx] != 0)
			Move(start, idx, next_cost, visited);
	}
	// Should come back to the start node
	if (visit_count == N && node == start)
		answer = min(answer, cost);
}

int main(void)
{
	// Get input
	cin >> N;
	input = vector<vector<int>>(N, vector<int>(N, 0));
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> input[i][j];
        }
    }

	vector<bool> visited(N, false);
	for (int v = 0; v < N; v++)
	{
		Move(v, v, 0, visited);
	}
	cout << answer;
	
	return 0;
}
