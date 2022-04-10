#include <iostream>

using namespace std;

int main(void)
{
	int x, y;
	scanf("%d %d", &x, &y);

	int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	char days_of_week[7][4] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

	int total_days = 0;
	for (int month = 1; month < x; ++month)
	{
		total_days += days[month - 1];
	}
	total_days += y;
	printf("%s", days_of_week[total_days % 7]);

	return 0;
}
