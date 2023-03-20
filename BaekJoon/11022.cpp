#include <iostream>

using namespace std;

int main(void)
{
	int T;
	cin >> T;
	int A, B;
	for (int i = 1; i <= T; i++)
	{
		cin >> A >> B;
		if (!(0 < A && A < 10) || !(0 < B && B < 10))
		{
			cout << "A, B is not valid.\n";
			return -2;
		}
		cout << "Case #" << i <<": " << A << " + " << B << " = " << A + B << '\n';
	}
}
