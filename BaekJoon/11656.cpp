#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	string S;
	cin >> S;
	int S_size = S.size();
	if (S_size > 1000)
	{
		cout << "Not valid string size.\n";
		return -1;
	}
	
	vector<string> dict;
	for (int i = 0; i < S_size; i++)
	{
		string str = S.substr(i, S_size - i);
		dict.push_back(str);
	}

	sort(dict.begin(), dict.end());
	
	for (auto element: dict)
	{
		cout << element << '\n';
	}
	return 0;
}
