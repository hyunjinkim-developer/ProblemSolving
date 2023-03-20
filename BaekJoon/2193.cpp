#include <iostream>
using namespace std;

int main(void)
{	
	int N;
	cin >> N;
	if (!(1 <= N && N <= 90))
	{
		cout << "Not valid N.\n";
		return -1;
	}
	
	long long **arr = new long long *[N + 1];
	for (int i = 0; i <= N; i++)
	{
		arr[i] = new long long[2];
	}
	arr[1][0] = 0;
	arr[1][1] = 1;

	for (int i = 2; i <= N; i++)
	{
		arr[i][0] = arr[i - 1][0] + arr[i - 1][1];
		arr[i][1] = arr[i - 1][0];
	}
	cout << arr[N][0] + arr[N][1];
	return 0;

}
