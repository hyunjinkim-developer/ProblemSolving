#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

bool cmp(const pair<long long, int> &a, const pair<long long, int> &b)
{
	if (a.second != b.second)
		return a.second > b.second;
	else
		return a.first < b.first;
}

int main(void)
{
	// faster input
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;
	if (!(1 <= N && N <= 100000))
	{
		cout << "Not valid number of cards.\n";
		return -1;
	}

	unordered_map<long long, int> cards;
	long long num;	
	for (int i = 0; i < N; i++)
	{
		cin >> num;
		cards[num]++;
	}

	vector<pair<long long, int>> vec(cards.begin(), cards.end());
	sort(vec.begin(), vec.end(), cmp);
	
	cout << vec[0].first;
	return 0;
}
