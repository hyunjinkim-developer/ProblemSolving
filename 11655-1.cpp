#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	// for faster input
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string S;
	getline(cin, S);
	int S_size = S.size();
	if (S_size > 100)
	{
		cout << "Not valid input size.\n";
		return -1;
	}
	for (int i = 0; i < S_size; i++)
	{
		if (('a' <= S[i] && S[i] <= 'z') || ('A' <= S[i] && S[i] <= 'Z'))
		{
			int temp;
			if ('a' <= S[i])
			{
				temp = (S[i] - 'a' + 13) % 26;
				cout << char(temp + 'a');
			}
			else
			{
				temp = (S[i] - 'A' + 13) % 26;
				cout << char(temp + 'A');
			}
		}
		else if (('0' <= S[i] && S[i] <= '9') || S[i] == ' ')
		{
			cout << S[i];
		}
		else
		{
			cout << "Not valid input character.\n";
			return -1;
		}
	}
	return 0;
}
