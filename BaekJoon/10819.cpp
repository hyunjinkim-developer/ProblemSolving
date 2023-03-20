/*
   Using next_permutation in <algorithm> header
*/
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int N;
	cin >> N;
	vector<int> input(N);
	for (int i = 0; i < N; i++)
	{
		cin >> input[i];
	}

	int answer = 0;
	int sum;
	int count = 0;
	sort (input.begin(), input.end());
	do
	{
		sum = 0;
		for (int i = 0; i < N - 1; i++)
		{
			sum += abs(input[i] - input[i + 1]); 
		}
		answer = max(answer, sum);
	} while(next_permutation(input.begin(), input.end()));

	cout << answer;
	return 0;
}
