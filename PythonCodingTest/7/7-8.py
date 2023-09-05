# Parametric search using binary search with iteration

# N: the number of rice cakes
# M: sizes of rice cakes
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    # Sum of spliced rice cake is not enough
    if total < m:
        end = mid - 1
    # Sum of spliced rice cake is more than enough
    else:
        result = mid
        start = mid + 1
print(result)