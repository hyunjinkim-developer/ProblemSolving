#include <iostream>

using namespace std;

int main(void)
{
	int R, C;
	cin >> R >> C;
	if (!(2 <= R && R <= 1000) || !(2 <= C && C <= 1000))
	{
		cout << "Not valid C or R.\n";
		return -1;
	}

	//int min = 0;
	//int minX = -1, minY = -1;
	int **input = new int *[R];
	for (int i = 0; i < R; i++)
	{
		input[i] = new int[C];
	}
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if 
			cin >> input[i][j];
		}
	}

	if (R % 2 == 1) // Row is odd
	{
		for (int row = 0; row < R; row++)
		{
			if(row % 2 == 0)
			{
				for (int col = 0; col <= C - 2; col++)
				{
					cout << "R";
				}
			}
			else
			{
				for (int col = C - 1; col >= 1; col--)
				{
					cout << "L";
				}
			}

			if (row != R - 1)
			{
				cout << "D";
			}
		}
	}
	else // Row is even
	{
		for (int row = 0; row <= R - 2; row++)
		{
			if (row == R - 2)
			{
				bool evenCol = C % 2 == 0 ?  true : false;
				//cout << evenCol << endl;
				for (int col = 0; col <= C - 1; col++)
				{
					if (col == C - 2 && evenCol == true)
					{
						string last =  input[R - 1][C - 2] > input[R - 2][C - 1] ? "DR" : "RD";
						cout << last;
						break;
					}

					if (col % 2 == 0)
					{
						cout << "D";
					}
					else
					{
						cout << "U";
					}
					if (col != C - 1)
						cout << "R";
				}
			}
			else
			{
				if (row % 2 == 0)
				{
					for (int col = 0; col <= C - 2; col++)
					{
						cout << "R";
					}
				}
				else
				{
					for (int col = C - 1; col >= 1; col--)
					{
						cout << "L";
					}
				}
				if (row != R - 2 || row != R - 1)
				{
					cout << "D";
				}
			}
		}
	}
	cout << "\n";

	return 0;
}
