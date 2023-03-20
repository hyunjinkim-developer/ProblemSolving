#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

#define N 100000

int main(void)
{
	string str;
	cin >> str;
	vector<char> input(str.begin(), str.end());
	int length = input.size();
	if (length > N || input[0] == 0)
	{
		cout << "Not valid N.\n";
		return -1;
	}

	int sum = 0;
	int numZero = 0;
	for (int i = 0; i < length; i++)
	{
		if (input[i] == '0')
		{
			numZero++;
		}
		sum += input[i];
	}
	// Right end digit should be zero
	if (numZero == 0)
	{
		cout << "-1";
	}
	// The sum of all digits should be multiple of 3
	else if (sum % 3 != 0)
	{
		cout << "-1";
	}
	else
	{
		// Find biggest number of all possible multiple of 30
		// Maximum number of input is 10^5, can not be calculate as
		// unsigned integer: 10 digits, unsigned long long: 20 digits
		sort(input.begin(), input.end(), greater<int>());

		for (auto element: input)
		{
			cout << element;
		}
	}

	return 0;
}
