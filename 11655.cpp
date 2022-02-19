#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	string S;
	getline(cin, S);
	int S_size = S.size();
	if (S_size > 100)
	{
		cout << "Not valid input length.\n";
		return -1;
	}

	// Encrypt with ROT13
	for (int i = 0; i < S_size; i++)
	{
		if ('a' <= S[i] && S[i] <= 'z')
		{
			int convert = S[i] + 13; // char range -128 ~ 127
			if (convert > 'z')
			{
				S[i] = ('a' - 1) + (convert % 'z');
			}
			else
			{
				S[i] = convert;
			}
		}
		else if ('A' <= S[i] && S[i] <= 'Z')
		{
			S[i] += 13;
			if (S[i] > 'Z')
			{
				S[i] = ('A' - 1) + (S[i] % 'Z');
			}
		}
		else if (('0' <= S[i] && S[i] <= '9') || S[i] == ' ')
		{
			continue;
		}
		else
		{
			cout << "Not valid input character.\n";
			return -1;
		}
	}

	// Print after Encryption
	for (auto ele: S)
	{
		cout << ele;
	}
	return 0;
}
