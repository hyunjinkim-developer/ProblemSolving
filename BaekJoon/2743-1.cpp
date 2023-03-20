#include <iostream>

using namespace std;

int main(void)
{
	char input[101];
	cin >> input;
	int i = 0;
	while (char c = input[i])
	{
		if (!(('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z')))
		{
			cout << "Input contains non-alphabet character.\n";
			return -1;
		}
		i++;
	}
	cout << i;
	return 0;
}
