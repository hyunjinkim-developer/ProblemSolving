/*
   Using quicksort
   https://www.geeksforgeeks.org/quick-sort/
*/

#include <iostream>

using namespace std;

/*
   a utility function to swap to two elements
 */
void swap(int *a, int *b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

/*
   This function takes last element as pivot,
   places the pivot element at its correct position in sorted array,
   and palces all smaller (smaller than pivot) to left of pivot
   and all greater elments to right of pivot
 */
int partition(int input[], int low, int high)
{
	int pivot = input[high];
	// Index of smaller element
	// and indicates the right position of pivot found so far
	int i = low - 1;

	for (int j = low; j <= high - 1; ++j)
	{
		// If current element is smaller than the pivot
		if (input[j] < pivot)
		{
			++i; // increment index of smaller element
			swap(&input[i], &input[j]);
		}
	}
	swap(&input[i + 1], &input[high]);
	return i + 1;
}

/* 
   input[] --> array to be sorted,
   low --> starting index,
   hight --> ending index
*/
void quick_sort(int input[], int low, int high)
{
	if (low < high)
	{
		// partitioning index: pivot
		// input[pivot] is now at right place
		int pi = partition(input, low, high);

		// separately sort element before and after pivot
		quick_sort(input, low, pi - 1);
		quick_sort(input, pi + 1, high);
	}
}

int main(void)
{
	int N;
	scanf("%d", &N);
	int *input = new int[N];
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &input[i]);
	}

	quick_sort(input, 0, N - 1);
	printf("%d %d", input[0], input[N - 1]);
	
	return 0;
}
