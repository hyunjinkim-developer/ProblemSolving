#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int N;
	scanf("%d", &N);
	vector<int> input(N);
	int num;
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &num);
		input[i] = num;
	}

	sort(input.begin(), input.end());

	printf("%d %d", input[0], input[N - 1]);

	return 0;
}
