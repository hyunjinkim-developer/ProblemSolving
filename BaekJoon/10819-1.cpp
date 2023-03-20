/*
   Make next_permutation function recursively
   https://www.codeguru.com/cplusplus/permutations-in-c/
*/

#include <iostream>
#include <vector>

using namespace std;

template <typename Func>

void permutation(vector<int> &input, vector<int> next, Func func, int *answer)
{
	int size = input.size();
	if (size > 0)
	{
		for (int cnt = 0; cnt < size; ++cnt)
		{
			vector<int> vt;
			vector<int>::const_iterator it = input.begin();
			for (int cnt1 = 0; cnt1 < size; ++cnt1)
			{
				if (cnt1 == cnt)
				{
					++it;
					continue;
				}
				else
				{
					vt.push_back(*it);
					++it;
				}
			}

			vector<int>::const_iterator it1 = input.begin();
			--it1;
			for (int cnt2 = 0; cnt2 <= cnt; ++cnt2)
			{
				++it1;
			}

			next.push_back(*it1);
			/*
			cout << "vt\n";
			for (auto ele: vt)
				cout << ele << " ";
			cout << endl;
			cout << "next\n";
			for (auto ele: next)
				cout << ele << " ";
			cout << endl <<"----------------" << endl ;
			*/
			permutation(vt, next, func, answer);
			//cout << "*************" << endl;
			next.pop_back();
		}
	}
	else
	{
		func(next, answer);
	}
}

void findMax(vector<int> perm, int *answer)
{
	int sum = 0;
	for (vector<int>::iterator it = perm.begin(); it != perm.end() - 1; ++it)
	{
		sum += abs(*it - *(it + 1));
	}
	*answer = max(sum, *answer);
/*	cout << "Total \n" << endl;
	for (vector<int>::iterator it = perm.begin(); it != perm.end(); ++it)
	{
		cout << *it << " ";
	}
	cout << endl;
	*/
}

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
	vector<int> vnext;
	permutation(input, vnext, findMax, &answer);
	cout << answer;

	return 0;
}
