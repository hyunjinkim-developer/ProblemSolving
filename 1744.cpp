#include <algorithm>
#include <iostream>
#include <deque>

using namespace std;

// Multiply positive, negative numbers separately
// In increase order of absolue value
int multiply(deque<int> &group)
{
	int count = group.size();
	int result = 0;
	int first, second;
	while (count > 1)
	{
		first = group.front();
		group.pop_front();
		second = group.front();
		group.pop_front();
/**/		
		if (first == 1 || second == 1)
		{
			if(first == 1)
				count--;
			if (second == 1)
				count--;
			continue;
		}
		result += first * second;
		count -= 2;
	}
	
	return result;
}

// Multiply negative numbers with zeors
void removeNegative(deque<int> &negative, int zeros)
{
	int size = negative.size();
	while (zeros > 0 && size > 0)
	{
		negative.pop_front();
		zeros--;
	}
}

// Add all of the remaining numbers
int addAll(deque<int> &positive, deque<int> &negative, int ones)
{
	int result = 0;
	int posCount = positive.size();
	int negCount = negative.size();

	while (posCount > 0)
	{
		result += positive.front();
		positive.pop_front();
		posCount--;
	}
	while (negCount > 0)
	{
		result += negative.front();
		negative.pop_front();
		negCount--;
	}
	while (ones > 0)
	{
		result += 1;
		ones--;
	}
	return result;
}

int main(void)
{
	int N;
	cin >> N;
/*
	if (!(1 <= N && N < 50))
	{
		cout << "Not valid N.\n";
		return -1;
	}
*/
	deque<int> positive, negative;
	int zeros = 0;
	int ones = 0;
	int input;
	for (int i = 0; i < N; i++)
	{
		cin >> input;
/*
		if (!(-1000 <= input && input <= 1000))
		{
			cout << "Not valid.input.\n";
			return -1;
		}
*/
		if (input == 0) // To multiply negative numbers with zero
		{
			zeros++;
		}
		else if (input == 1) // 1 + 1 > 1 * 1
		{
			ones++;
		}
		else if (input > 0)
		{
			positive.push_back(input);
		}
		else
		{
			negative.push_back(input);
		}
	}
	
	// Sort in increase order of absolute value
	sort(positive.begin(), positive.end(), greater<int>());
	sort(negative.begin(), negative.end());

	int ans = 0;
	ans += multiply(positive);
	ans += multiply(negative);
	removeNegative(negative, zeros);
	ans += addAll(positive, negative, ones);
	cout << ans;

	return 0;
}
