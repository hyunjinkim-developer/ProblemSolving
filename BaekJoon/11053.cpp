#include <iostream>

using namespace std;

int main(void)
{
	int N;
	cin >> N;
	if (!(1 <= N && N <= 1000))
	{
		cout << "Not valid N.\n";
		return -1;
	}
	int input[N];
	for (int i = 0; i < N; i++)
	{
		cin >> input[i];
	}
	int *subse = new int[N + 1];
	int idx = 0;
	for (int i = 0; i < N; i++)
	{
		if (input[i] > subse[idx])
		{
			++idx;
			subse[idx] = input[i];
		}
		else
		{
			for (int j = idx; j >= 0; j--)
			{
				if (subse[j] >= input[i])
					continue;
				else
				{
					subse[j + 1] = input[i];
					break;
				}
			}
		}
	}
	cout << idx;

	return 0;
}
