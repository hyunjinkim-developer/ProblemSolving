#include <iostream>

using namespace std;

// When R is odd, C is even or odd
void moveHorizental(int R, int C, string &result)
{
	for (int row = 0; row < R; row++)
	{
		// Move R
		if (row % 2 == 0)
		{
			for (int col = 0; col <= C - 2; col++)
			{
				result.append("R");
			}
		}
		// Move L
		else
		{
			for (int col = C - 1; col >= 1; col--)
			{
				result.append("L");
			}
		}
		// Move D, except last move of last row
		if (row != R - 1)
		{
			result.append("D");
		}
	}
}

// When R is even, C is odd
void moveVertical(int R, int C, string &result)
{
	for (int col = 0; col < C; col++)
	{
		// Move D
		if (col % 2 == 0)
		{
			for (int row = 0; row <= R - 2; row++)
			{
				result.append("D");
			}
		}
		// Move U
		else
		{
			for (int row = R - 1; row >= 1; row--)
			{
				result.append("U");
			}
		}
		// Move R, except last move of last col
		if (col != C - 1)
		{
			result.append("R");
		}
	}
}

int * findMin(int R, int C, int **input)
{
	int *minPos = new int[2];
	int minval = 1000;

	for (int row = 0; row < R; row++)
	{
		for (int col = 0; col < C; col++)
		{
			if ((row + col) % 2 == 1)
			{
				int cur = input[row][col];
				if (cur < minval)
				{
					minval = cur; 
					minPos[0] = row;
					minPos[1] = col;
				}
			}
		}
	}
	return minPos;
}

void move2RowHorizontal(int C, int direction, string &result)
{
	if (direction == 1) // Move -> D  <-
	{
		for (int col = 0; col <= C - 2; col++)
		{
			result.append("R");
		}
		result.append("D");
		for (int col = C - 1; col >= 1; col--)
		{
			result.append("L");
		}
	}
	else if (direction == -1) // Move <- D ->
	{
		for (int col = C - 1; col >= 1; col--)
		{
			result.append("L");
		}
		result.append("D");
		for (int col = 0; col <= C - 2; col++)
		{
			result.append("R");
		}
	}
}

void move2RowVertical(int C, int *minPos, string &result)
{
	int skipR = minPos[0];
	int skipC = minPos[1];
	int vertical = -1; // -1: Down, 1: Up

	for (int col = 0; col < C; col++)
	{
		if (col != skipC) 
		{
			// Change vertical moving direction
			if (vertical == -1)
			{
				result.append("D");
				vertical = 1;
			}
			else 
			{
				result.append("U");
				vertical = -1;
			}
		}
		
		if (col != C - 1)
			result.append("R");
	}
}

int main(void)
{
	// Get R, C
	int R, C;
	cin >> R >> C;

	// Get Satisfaction values
	int **input = new int *[R];
    for (int i = 0; i < R; i++)
    {
        input[i] = new int[C];
    }
	int value;
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cin >> input[i][j];
        }
    }
	
	// Move to feel maximum satisfaction
	string result;	// Total movement
	// Row is odd
	if (R % 2 == 1)
	{
		moveHorizental(R, C, result);
	}
	// Row is even
	else
	{
		// Row is even, Col is odd
		if (C % 2 == 1)
		{
			moveVertical(R, C, result);
		}
		// Ros is even, Col is even
		else
		{
			// Find the smallest satisfaction value 
			// which will be not visited
			int *minPos = findMin(R, C, input);
			// Debug
			//cout << "min: "<< minPos[0]  << " " << minPos[1] << endl;

			int horizontal_dir = 1; // 1: Right, -1: Left
			int row = 0;
			while (row < R)
			{
				if (row == minPos[0] || row + 1 == minPos[0])
				{
					// move vertically 
					// without minimum satisfaction value
					move2RowVertical(C, minPos, result);
					horizontal_dir = -1;
				}
				else
				{
					// Move 2 row horizontally
					move2RowHorizontal(C, horizontal_dir, result);
				}
				
				if(row != R - 2)
				{
					result.append("D");
				}
				row += 2;
			}
		}
	}

	cout << result << endl;
	return 0;
}
