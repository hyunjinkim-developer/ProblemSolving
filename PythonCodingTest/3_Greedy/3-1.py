change = 1260
coins = [500, 100, 50, 10] # Sorted in DESC

count = 0

for coin in coins:
    count += change // coin
    change %= coin

print(count)
