#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool cmp(const vector<int> &a, vector<int> &b)
{
	if (a[1] == b[1])
	{
		// The shorter using time, the more people can use the room
		return a[0] < b[0];
	}
	// The eariler a meeting ends, the more people can use the room
	return a[1] < b[1];	
}

int main(void)
{
	int N;
	cin >> N;
	if (!(1 <= N && N <= 100000))
	{
		cout << "Not valid N.\b";
		return -1;
	}
	vector<vector<int>> input(N);
	for (int i = 0; i < N; i++)
	{
		input[i] = vector<int>(2);
		// input[][0]: starting time/ input[][1]: end time/
		cin >> input[i][0] >> input[i][1];
	}
	sort(input.begin(), input.end(), cmp);

	int answer = 1;
	int startTime = input[0][1];
	for (int i = 1; i < N; i++)
	{
		if (startTime <= input[i][0])
		{
			answer++;
			startTime = input[i][1];
		}
	}
	cout << answer;

	return 0;
}
