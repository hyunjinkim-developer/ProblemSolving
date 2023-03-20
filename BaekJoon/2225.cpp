// This code CAN NOT pass judge
// Solution in mathmatical way
// Max of N and K could be 200
// 200! is 375 digit 
// Calculation can not be handled in long long
#include <iostream>

#define div 1e9

using namespace std;

long long factorial(int n, long long *fact)
{
	if (n == 0)
		return fact[n] = 1;
	if (fact[n] != 0)
		return fact[n];
	return fact[n] = n * factorial(n - 1, fact);
}

long long combination(int n, int r, long long *fact)
{
	if (fact[n] == 0)
		factorial(n, fact);
	if (fact[r] == 0)
		factorial(r, fact);
	if (fact[n - r] == 0)
		factorial(n - r, fact);

	return fact[n] / (fact[r] * fact[n - r]);
}

int main(void)
{
	int N, K;
	scanf("%d %d", &N, &K);
	
	long long * fact = new long long [N + 1];
	
	long long answer = 0;
	long long possible_num_seq; // # of possible integers: k - i
	long long seq_including_zero;
	for (int i = 0; i <= K - 1; ++i) // i: number of possible zero
	{

		possible_num_seq = combination(N  - 1, K - i - 1, fact);
		seq_including_zero = factorial(K, fact) / (factorial(i, fact) * factorial(K - i, fact));
		answer += (possible_num_seq * seq_including_zero) % (long long) div;
	}

	printf("%lld", answer);
	return 0;
}
