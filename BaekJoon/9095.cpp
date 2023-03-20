// Top down: Using Recursion with memoization

#include <iostream>
#include <vector>

using namespace std;

int add(vector<int> &answer, int n)
{

	if (n == 1)
		return answer[1] = 1;
	else if (n == 2)
		return answer[2] = 2;
	else if (n == 3)
		return answer[3] = 4;
	else if (answer[n] != 0)
		return answer[n];
	
	return answer[n] = add(answer, n - 1) + add(answer, n - 2) + add(answer, n - 3);
}

int main(void)
{
	int T; // # of test case
	cin >> T;
	vector<int> answer(11, 0); // n is less than 11
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
			add(answer, n);
		}

		cout << answer[n] << '\n';
	}
	return 0;
}


