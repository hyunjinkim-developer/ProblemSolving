#include <iostream>

using namespace std;

int main(void)
{
	string input;
	while (getline(cin, input)) 
	{
		if (input == "")
			break;
		cout << input << endl;
	}
	return 0;
}
