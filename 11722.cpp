#include <cstring>
#include <iostream>

using namespace std;

int count(int idx, int *input, int *cache, const int N)
{
	int &ret = cache[idx];
	if (ret != -1)
		return ret;
	else
	{
		ret = 1;
		for (int i = idx + 1; i < N; i++)
		{
			if (input[idx] > input[i])
				ret = max(ret, 1 + count(i, input, cache, N));
		}
		return ret;
	}
}

int main(void)
{
	// Get input
	int N;
	scanf("%d", &N);
	if (!(1 <= N && N <= 1000))
	{
		printf("Not valid N.\b");
		return -1;
	}
	int *input = new int[N];
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &input[i]);
	}
	int *cache = new int[N];
	memset(cache, -1, N * sizeof(int));

	// Count subsequence
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		ans = max(ans, count(i, input, cache, N));
	}
	cout << ans;

	return 0;
}
