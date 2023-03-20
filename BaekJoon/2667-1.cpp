// Using BFS

#include <algorithm>
#include <iostream>
#include <list>
#include <vector>

using namespace std;

// void printVector(vector<vector<int>> vec, int size)
// {
//     for (int row = 0; row < size; row++)
//     {
//         for (int col = 0; col < size; col++)
//         {
//             cout << vec[row][col] << " ";
//         }
//         cout << '\n';
//     }
// }

int main(void)
{
    int N;
    scanf("%d", &N);
    if (!(5 <= N && N <= 25))
    {
        printf("Invalid N is typed.\n");
        return -1;
    }

    // Get map from User
    vector<vector<int>> map (N, vector<int>(N, 0));
    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
        {
            scanf("%1d", &map[row][col]);
        }
    }

    // Search with BFS
    // Check visited node
    vector<vector<int>> visited (N, vector<int>(N, 0));
    // Save next Node into list
    list<pair<int, int>> nextList;
    // Assign next move
    vector<vector<int>> nextMove = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Up, Down, Left, Right
    // number of complexes
    int numComplex = 0;
    // number of house in current complex
    vector<int> house;
    int numHouse = 0;
    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
        {
            if (map[row][col] == 1 && visited[row][col] == 0)
            {
                numComplex++;
                visited[row][col] = numComplex;
                numHouse++;
                nextList.push_back(pair<int, int> (row, col));

                while (!nextList.empty())
                {
                    pair<int, int> ele = nextList.front();
                    nextList.pop_front();

                    for (int next = 0; next < 4; next++)
                    {
                        int newRow = ele.first + nextMove[next][0];
                        int newCol = ele.second + nextMove[next][1];

                        if ( !((0 <= newRow && newRow <= N - 1) && (0 <= newCol && newCol <= N - 1)) )
                        {
                            continue;
                        }

                        if (map[newRow][newCol] == 1 && visited[newRow][newCol] == 0)
                        {
                            visited[newRow][newCol] = numComplex;
                            numHouse++;
                            nextList.push_back(pair<int, int> (newRow, newCol));
                        }
                    }
                }
                house.push_back(numHouse);
                numHouse = 0;
            }
        }
    }

    // Debug
    // printVector(visited, N);

    printf("%d\n", numComplex);
    sort(house.begin(), house.end());
    for (auto num : house)
    {
        cout << num << endl;
    }
    
    return 0;
}



/*
// Wook's Code
#include <algorithm>
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> graph(N, vector<int>(N, 0));
    for (int row = 0; row < N; row++) {
        string s;
        cin >> s;
        for (int col = 0; col < N; col++)
            graph[row][col] = s[col] - '0';
    }
            
    vector<int> components;
    vector<pair<int, int>> direction = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    
    for (int row = 0; row < N; row++)
        for (int col = 0; col < N; col++)
            if (graph[row][col]) {
                int cnt = 1;                
                deque<pair<int, int>> que(1, {row, col});
                graph[row][col] = 0;                
                
                while (!que.empty()) {
                    for (auto d : direction) {
                        int r = que.front().first + d.first;
                        int c = que.front().second + d.second;
                        if (0 <= r && r < N && 0 <= c && c < N && graph[r][c]) {
                            cnt++;
                            graph[r][c] = 0;
                            que.push_back({r, c});
                        }                        
                    }
                   que.pop_front();                                   
                }
                
                components.push_back(cnt);
            }
    
    sort(components.begin(), components.end());
    cout << components.size() << '\n';
    for (int c : components)
        cout << c << '\n';
    
    return 0;
}
*/