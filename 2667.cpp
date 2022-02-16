// Using DFS for searching

#include <iostream>
#include <list>
#include <vector>

using namespace std;

void printVisited(vector<vector<int>> visited, int N)
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			printf("%d ", visited[i][j]);
		}
		printf("\n");
	}
}

void DFS(int N, vector<vector<int>> map, vector<vector<int>> &visited, int &numComplex, int xPos, int yPos, int &house)
{
	visited[xPos][yPos] = numComplex;
	house++;

	// printVisited(visited, N);
	// cout << '\n';

	// Left, Right, Up, Down
	int move[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
	for (int i = 0; i < 4; i++)
	{
		int newxPos = xPos + move[i][0];
		int newyPos = yPos + move[i][1];

		if (!((0 <= newxPos && newxPos <= N-1) && (0 <= newyPos && newyPos <= N-1)))
		{
			continue;
		}

		if (map[newxPos][newyPos] == 1 && visited[newxPos][newyPos] == 0)
		{
			DFS(N, map, visited, numComplex, newxPos, newyPos, house);
		}
	}
}

int main(void)
{
	int N;
	scanf("%d", &N);
	if (!(5 <= N && N <= 25))
	{
		printf("N is not valid.\n");
		return -1;
	}

	vector < vector<int> > map (N);
	vector < vector<int> > visited (N, vector<int>(N, 0));
	string input;
	for (int i = 0; i < N; i++)
	{
		cin >> input;
		for (int j = 0; j < N; j++)
		{
			map[i].push_back(input[j] - '0');
		}
	}

	// number of complex
	int numComplex = 1;
	// list of num of houses in current complex
	list<int> numHouse;
	for (int xPos = 0; xPos < N; xPos++)
	{
		for (int yPos = 0; yPos < N; yPos++)
		{
			if (map[xPos][yPos] == 1 && visited[xPos][yPos] == 0)
			{
				int house = 0; // count houses of current complex
				DFS(N, map, visited, numComplex, xPos, yPos, house);
				numHouse.push_back(house); 
				numComplex++; 
			}
		}
	}

	cout << numComplex - 1 << endl;
	numHouse.sort();
	for (list<int>::iterator iter = numHouse.begin(); iter != numHouse.end(); iter++)
	{
		cout << *iter << endl;
	}

	return 0;
}
