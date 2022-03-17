#include <iostream>

using namespace std;

int R, C; // Row, Col of input

// Find the position with the smallest satisfaction value
int * findMinPosition(int **input)
{
	int min = 1000; // Input is an integer, less than 1000
	int *minPosition = new int[2];	
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if ((i + j) % 2 == 1)
			{
				if (input[i][j] < min)
				{
					min = input[i][j];
					minPosition[0] = i;
					minPosition[1] = j;
				}
			}
		}
	}
	return minPosition;
}

// Move 2 rows in horizentally 
void horizentalMove(int direction, int startR)
{
	if (startR == R - 1)
	{
		for (int col = 0; col <= C - 2; col++)
		{
			cout << "R";
		}
	}
	else
	{
		for (int row = startR; row < startR + 2; row++)
		{
			if (direction == 1) // Move R
			{
				for (int col = 0; col <= C - 2; col++)
				{ 
					cout << "R";
				}
				direction = -1;
			}
			else if (direction == -1) // Move L
			{
				for (int col = C - 1; col >= 1; col--)
				{
					cout << "L";
				}
				direction = 1;
			}
			if (row != R - 1)
				cout << "D";
		}
	}
}

// Move 2 cols in vertically
bool verticalMove(int minPosC, int startRow)
{
	int direction = -1;
	for (int col = 0; col <= C - 1; col++)
	{
		// In position that has smallest satisfaction value
		if (col == minPosC)
		{
			if (col == C - 1)
				continue;

			cout << "R";
			continue;
		}

		if (direction ==  -1)
		{
			cout << "D";
			direction = 1;
		}
		else if (direction == 1)
		{
			cout << "U";
			direction = -1;
		}
		if (col != C - 1)
		{
			cout << "R";
		}
	}
	if (startRow + 1 != R - 1)
	{
		cout << "D";
	}
	return true;
}

int main(void)
{
	// Get input
	cin >> R >> C;
	if (!(1 <= R && R <= 1000) || !(2 <= C && C <= 1000))
	{
		cout << "Not valid C or R.\n";
		return -1;
	}
	int **input = new int *[R];
    for (int i = 0; i < R; i++)
    {   
        input[i] = new int[C];
    }   
    for (int i = 0; i < R; i++)
    {   
        for (int j = 0; j < C; j++)
        {   
            cin >> input[i][j];
        }   
    }
	
	bool evenRow = (R % 2 == 0) ? true : false;
	bool evenCol = (C % 2 == 0) ? true : false;
	int moveRL = 1; // R: 1, L: -1


	if (evenRow)
	{
		if (evenCol) // Row is even, Col is even
		{
			int *minPos = findMinPosition(input);
//	cout << endl << minPos[0] << ", " << minPos[1] << endl; 
			bool remove = false;
			for (int row = 0; row < R; row++)
			{
				if (row % 2 == 0)
				{
					if (minPos[0] == row || minPos[0] == row + 1)
					{
						remove = verticalMove(minPos[1], row);
					}
					else
					{
						if (remove)
						{
							moveRL = -1;
							remove = false;
						}
						horizentalMove(moveRL, row);
						

						if (moveRL == 1)
							moveRL = -1;
						else if (moveRL == -1)
							moveRL = 1; 
					}
				}
			}
		}
		else // Row is even, Col is odd
		{
			for (int col = 0; col <= C - 1; col++)
			{
				if (col % 2 == 0)
				{
					for (int row = 0; row <= R - 2; row++)
					{
						cout << "D";
					}
				}
				else
				{
					for (int row = R - 1; row >= 1; row--)
					{
						cout << "U";
					}
				}
				if (col != C - 1)
					cout << "R";
			}
		}
	}
	else // Row is odd
	{

		for (int row = 0; row < R; row++)
		{
			if (row % 2 == 0)
			{
				horizentalMove(moveRL, row);

				if (moveRL == 1)
					moveRL = -1;
				else if (moveRL == -1)
					moveRL = 1;
			}
		}
	}
	cout << endl;
	return 0;
}
