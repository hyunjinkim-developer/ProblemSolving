// Not qualified time limit

#include <iostream>
#include <map>

#define FasterIO ios_base::sync_with_stdio(false); cin.tie(NULL);
using namespace std;

void remove_side(multimap<int, pair<int, int>, greater<int>> &stickers, const multimap<int, pair<int, int>, greater<int>>::iterator iter, int n)
{
	int posY = (iter -> second).first;
	int posX = (iter -> second).second;
	int remove[4][2] = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
	for (int i = 0; i < 4; i++)
	{
		int newX = posX + remove[i][0];
		int newY = posY + remove[i][1];
		if (!(0 <= newX && newX <= n - 1))
		{
			continue;
		}
		if (!(0 <= newY && newY <= 1))
		{
			continue;
		}
		// remove stickers that locate side of a sticker that is picked
		for (auto it = stickers.begin(); it != stickers.end(); it++)
		{
			if ((it -> second).first == newY && (it -> second).second == newX)
			{
				stickers.erase(it);
				break;
			}
		}
	}

}

int main(void)
{
	FasterIO;
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int n;
		cin >> n;
		if (!(1 <= n && n <= 100000))
		{
			cout << "Not valid n.\n";
			return -1;
		}
		multimap<int, pair<int, int>, greater<int>> stickers;
		for (int j = 0; j < 2; j++)
		{
			for (int i = 0; i < n; i++)
			{
				int value;
				cin >> value;
				if (!(0 <= value  && value <= 100))
				{
					cout << "Not valid n.\n";
					return -1;
				}
				stickers.insert(make_pair(value, make_pair(j, i)));
			}
		}
		
		int answer = 0;
		while (!stickers.empty())
		{
			auto iter = stickers.begin();
			answer += iter -> first;
			remove_side(stickers, iter, n);
			stickers.erase(iter);
		}
		cout << answer << endl;
	}
		return 0;
}
