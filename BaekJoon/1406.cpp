#include <list>
#include <iostream>
#include <iterator>
#include <string>

using namespace std;

int main(void)
{
	string input;
	cin >> input;
	list<char> str;
	str.insert(str.begin(), input.begin(), input.end());
	
	int M;
	cin >> M;
	// Cursor locates at the end of str before editing
	list<char>::iterator iter = str.end();
	char order;
	for (int i = 0; i < M; i++)
	{
		cin >> order;
		switch(order)
		{
			// Move the cursor to the left
			// it the cursor is located at the left end, do not move the cursor
			case 'L':
				if (iter != str.begin())
				{	
					iter = prev(iter, 1);
				}
				break;

			// Move the cursor to the right
			// if the cursor is located at the right end, do not move the cursor
			case 'D':
				if (iter != str.end())
				{
					iter = next(iter, 1);
				}
				break;

			// Remove letter on the left of the cursor
			// if the cursor is located at the left end 
			// no letter is removed
			case 'B':
				if (iter != str.begin())
				{
					iter = prev(iter, 1);
					iter = str.erase(iter);
				}
				break;

			// Insert letter on the left of the cursor
			case 'P':
				char letter;
				cin >> letter;
				iter = str.insert(iter, letter);
				if (iter != str.end())
				{
					iter = next(iter, 1);
				}
				break;
		}
	}
	
	// Print output
	for (auto ele: str)
		cout << ele;
	return 0;
}
