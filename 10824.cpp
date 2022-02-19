#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	// for faster input
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string A, B, C, D;
	cin >> A >> B >> C >> D;
	int a = stoi(A), b = stoi(B), c = stoi(C), d = stoi(D);
	if (!(1 <= a && a <= 1000000) || !(1 <= b && b <= 1000000) || !(1 <= c && c <= 1000000) || !(1 <= d && d <= 1000000))
	{
		cout << "Not valid A, B, C or D.\n";
		return -1;
	}

	cout << stoll(A + B) + stoll(C + D);

	return 0;
}
