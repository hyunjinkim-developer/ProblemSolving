// Bottom up

#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int T;
	cin >> T;
	vector<int> answer(11, 0);
	answer[1] = 1;
	answer[2] = 2;
	answer[3] = 4;
	int n;
	for (int i = 0; i < T; i++)
	{
		cin >> n;
		if (!(0 < n && n < 11))
		{
			cout << "Not valid n.\n";
			return -1;
		}

		if (answer[n] == 0)
		{
			for (int j = 4; j <= n; j++)
			{
				answer[j] = answer[j - 1] + answer[j - 2] + answer[j - 3];
			}
		}
		cout << answer[n] << '\n';
	}

	return 0;
}
