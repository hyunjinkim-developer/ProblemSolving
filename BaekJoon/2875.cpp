#include <iostream>

using namespace std;

int main(void)
{
	int N, M, K;
	cin >> N >> M >> K;
	if (!(0 <= N && N <= 100))
	{
		cout << "Not valid N.\n";
	}
	if (!(0 <= M && M <= 100))
	{
		cout << "Not valid M.\n";
		return -1;
	}
	if (!(0 <= K && K <= M+N))
	{
		cout << "Not valid K.\n";
		return -1;
	}
	int Mteam = N / 2;
	int Fteam = M;
	int max_team = min(Mteam, Fteam);
	int left;
	for (int i = max_team; i >= 0; i--)
	{
		left = M + N - (i * 3);
		if (left >= K)
		{
			max_team = i;
			break;
		}
	}
	cout << max_team;

	return 0;
}
