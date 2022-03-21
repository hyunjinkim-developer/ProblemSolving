#include <iostream>

using namespace std;

// Find nearest number from N whose every digit is working
bool check(int cur, const bool *notworking)
{
	string curstr = to_string(cur);
	int curlength = curstr.size();
	for (int i = 0; i < curlength; i++)
	{
		if (notworking[curstr[i] - '0'])
			return false;
	}
	return true;
}

int main(void)
{
	int N, M;
	cin >> N;
	cin >> M;
	bool notworking[10] = {false};
	int num;
	if (M != 0)
	{
		for (int i = 0; i < M; i++)
		{
			cin >> num;
			notworking[num] = true;
		}
	}
	
	int minCount = abs(N - 100);
	// Find nearest number from N whose every digit is working
	for (int i = 0; i <= 1000000; i++) // Nearest number can be smaller or bigger than N
	{
		if (check(i, notworking))
		{
			int count = abs(N - i) + to_string(i).size();
			minCount = min(minCount, count);
		}
	}
	cout << minCount;

	return 0;
}
