#include <iostream>

using namespace std;

int main(void)
{
    int E, S, M;

    // get input: 1 ≤ E ≤ 15,  1 ≤ S ≤ 28, 1 ≤ M ≤ 19
    do
    {
        scanf("%d %d %d", &E, &S, &M);
    } while(!(1 <= E && E <= 15) || !(1 <= S && S <= 28) || !(1 <= M && M <= 19));

    // count year
    int cE = 0, cS = 0, cM = 0;
    int year = 0;
    while (!(cE == E && cS == S && cM == M))
    {
        cE++;
        cS++;
        cM++;
        year++;

        if (cE > 15)
        {
            cE = 1;
        }
        if (cS > 28)
        {
            cS = 1;
        }
        if (cM > 19)
        {
            cM = 1;
        }
    }
    cout << year;
}