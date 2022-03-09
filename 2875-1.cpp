// Wook's code

#include <iostream>

using namespace std;

int main(void)
{
	int N, M, K;
	cin >> N >> M >> K;

	// remove K from N or M which is bigger than the other 
	for (int i = 0; i < K; i++)
	{
		if (N > M * 2)
			N--;
		else if (N <= M * 2)
			M--;
	}
	
	// Print out N or M which makes smaller team 
	// the number of team depends on pairs of men's team end woman's team
	cout << (N / 2 > M ? M : N / 2);

	return 0;
}
