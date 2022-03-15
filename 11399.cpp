#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool cmp (const pair<int, int> & a, const pair<int, int> & b)
{
	return a.second < b.second;
}

int main(void)
{
	int N;
	cin >> N;
	if (!(1 <= N && N <= 1000))
	{
		cout << "Not valid N.\n";
		return -1;
	}
	vector<pair<int, int>> input;
	int time;
	for (int  i = 0; i < N; i++)
	{
		cin >> time;
		input.push_back(pair(i, time));
	}

	sort(input.begin(), input.end(), cmp);
	
	int cur = 0;
	int answer = 0;
	for (int i = 0; i < N; i++)	
	{
		cur += input[i].second;
		answer += cur;
	}
	cout << answer;
	return 0;
}
