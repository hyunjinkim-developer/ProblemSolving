#include <algorithm>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

// Calculate nextNum
int nextNum(int prevNum, int P)
{
    // nextNum that will be added to the Vector p
    int nextNum = 0;
    
    int digit = 0;
    int prev = prevNum;
    while (prev)
    {
        prev /= 10;
        digit++;
    }
 
    for (int i = digit - 1; i >= 0; i--)
    {
        int curDigit = prevNum / pow(10, i);
        prevNum = prevNum % (int) pow(10, i); 
        nextNum += pow(curDigit, P);
    }

    return nextNum;
}

// Find whether nextNum is in p 
// if found return true, else return false
bool contains(vector<int> p, int nextNum, int *N)
{
    bool found = false;
    vector<int>::iterator iter;

    // int iterN = 0;
    for (iter = p.begin(); iter != p.end() - 1; iter++)
    {
        if (*iter == nextNum)
        {
            found = true;
            // *N = iterN;
            // Get index from iterator 
            *N = iter - p.begin();
            break;
        } 
        // iterN++;   
    }

    return found;
}

int usingVector(int A, int P)
{
    // Vector of permutation 
    vector<int> p;
    // vector<int>::iterator iter;
    p.push_back(A);
    // number of elements that are not overlapped in permutation
    int N = 0;

    while (!contains(p, p.back(), &N))
    {
        p.push_back(nextNum(p.back(), P));
    }

    return N;
}

int main(void)
{
    int A, P;
    // Get A, P
    // A: starting number
    // P: exponent of each digit
    do
    {
        scanf("%d %d", &A, &P);
    } while (!(1 <= A && A <= 9999) || !(1 <= P && P <= 5));

    // // Using Vector
    cout << usingVector(A, P);
}