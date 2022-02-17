#include <iostream>

using namespace std;

int main(void)
{
	string input;
	cin >> input;
	if (!(input.size() <= 100))
	{
		cout << "Not valid input length.\n";
		return -1;
	}
	int i = 0;
	while (input[i])
	{
		if (!isalpha(input[i]))
		{
			cout << "Input contains non-alphabet letters.\n";
			return -1;
		}
		i++;
	}
	cout << input.size();

	return 0;
}
