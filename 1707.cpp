// Solve with BFS

#include <iostream>
#include <list>

using namespace std;

void printVisited(int *visited, int V)
{
    for (int i = 1; i <= V; i++)
    {
        cout << visited[i] << " ";
    }         
}

bool visitedAll(int *visited, int V)
{
    int count = 0;
    for (int i = 1; i <= V; i++)
    {
        if (visited[i] != 0)
        count++;
    }
    if (count == V)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int findNextNode(int *visited, int V)
{
    int next = -1;
    for (int i = 1; i <= V; i++)
    {
        if (visited[i] == 0)
        {
            next = i;
            break;
        }
    }
    return next;
}

int main(void)
{
    int K; // # of test case
    do
    {
        scanf("%d", &K);
    } 
    while (!(2 <= K && K <= 5));

    int V, E; 
    list<int> *adj;
    // Used to move onto next test case 
    // if current test case is not bipartite graph
    int flag = 0; 
    for (int i = 0; i < K; i++)
    {
        int flag = 0;
        scanf("%d %d", &V, &E); // Get # of vertices, and # of edges
        adj = new list<int>[V+1];
        int u, v;
        for (int j = 0; j < E; j++) // Get edges
        {
            do
            {
                scanf("%d %d", &u, &v);
            } while (u == v);
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        // Mark all the vertices are not visited in 0
        // If a vertex visited and colored in 1
        // adjacent vertex colored in -1
        int *visited = new int[V+1];
        for (int vertex = 1; vertex <= V; vertex++)
        {
            visited[vertex] = 0;
        }
        
        // Create a queue for BFS
        list<int> queue;

        // iterator 'i' will be used to get
        // all adjacent vertices of a vertex
        list<int>::iterator iter;
        while (!visitedAll(visited, V))
        {
            int next = findNextNode(visited, V);
            visited[next] = 1;
            queue.push_back(next);
            
            while (!(queue.empty()))
            {
                // Dequeue a vertex from queue
                int currentV = queue.front();
                queue.pop_front();

                // Get all adjacent vertices of 
                // the dequeued vertex currentV
                // If a adjacent has not been visitied,
                //then mark it with different color with currentV
                //and enqueue it
                for (iter = adj[currentV].begin(); iter != adj[currentV].end(); iter++)
                {
                    int adjVertex = *iter;

                     // If current test case is not bipartite graph
                    // move onto next test case
                    if (visited[currentV] == visited[adjVertex])
                    {
                        flag = -1;
                    }

                    if (visited[adjVertex] == 0)
                    {
                        if (visited[currentV] == -1)
                        {
                            visited[adjVertex] = 1;
                        }
                        else if (visited[currentV] == 1)
                        {
                            visited[adjVertex] = -1;
                        }
                        queue.push_back(adjVertex);
                    }   
                }
            // // Debug
            //     cout << endl << currentV << endl;
            //     printVisited(visited, V);   
            }
            if (flag == -1)
            {
                cout << "NO" << endl;
                break;
            }
        }
        if (flag == 0)
        {
            cout << "YES" << endl;
        }

        adj->clear();
        queue.clear();
    }
}




/* other's code
#include <iostream>
#include <map>

using namespace std;

int power(int num, int P) {
    int result = 1;
    for (int i = 0; i < P; i++)
        result *= num;
    return result;
}

int generate(int num, int P) {
    int result = 0;
    while(num) {
        result += power(num % 10, P);
        num /= 10;
    }
    return result;
}

int main() {
    int A, P;
    
    cin >> A >> P;
    
    map<int, int> sequence;
    for (int i = 0; !sequence.count(A); i++) {
        sequence[A] = i;
        A = generate(A, P);
    }
    
    cout << sequence[A];
    
    return 0;
}
*/