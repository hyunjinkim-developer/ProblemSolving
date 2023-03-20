#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int N, K;
	cin >> N >> K;
	if (!(1 <= N && N <= 10) || !(1 <= K && K <= 100000000))
	{
		cout << "Not valid N, K, or both.\n";
		return -1;
	}
	vector<int> coins(N);
	for (int i = 0; i < N; i++)
	{
		cin >> coins[i];
	}

	int answer = 0;
	for (int i = N - 1; i >= 0; i--)
	{
		if (K == 0)
			break;
		// Question's condition:
		// A1 = 1, in case of i >= 2 Ai is multiple of Ai-1
		answer += K / coins[i];
		K = K % coins[i];
	}
	cout << answer;

	return 0;
}
