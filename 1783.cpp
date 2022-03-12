#include <iostream>

using namespace std;

int main(void)
{
    // board[0]: #of row, board[1]: # of col
    int board[2];
    cin >> board[0] >> board[1];
    int &y = board[0];
    int &x = board[1];
	
	int visited;
	if (y == 1)
	{
		// Cannot move
		visited = 1;
	}
	else if (y == 2)
	{
	//	1(Starting point) + (x - 1) / 2
		visited = min(4, 1 + (x - 1) / 2);
	}
	else
	{
		if (x < 7)
		{
		//	 1(Starting point) + (x - 1)
			visited = min(4, x);
		}
		else
		{
			x -= 7;
			y -= 7;
			visited += 5; // Starting point + mandated 4 moves
			visited += x;
		}
	}
	cout << visited;

	return 0;
}
