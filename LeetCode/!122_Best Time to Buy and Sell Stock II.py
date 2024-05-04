"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""

# Solution1 :
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])

        return profit

# Solution 2:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Solution 1
        # profit = 0
        # for i in range(1, len(prices)):
        #     profit += max(0, prices[i] - prices[i - 1])

        # return profit

        HOLD, SELL = 0, 1
        ## Dictionary (Hash table)
        # key: (day, state) pair
        # value: coreesponding maximal profit
        dp  = {}

        # No free lunch, it is impoosible to have stock before first trading day
        dp[-1, HOLD] = -math.inf
        # No gain, no loss before first trading day
        dp[-1, SELL] = 0

        for day, stock_price in enumerate(prices):
            # If today we have stock,
            # either we already had it yesterday, or we just buy stock and hold it today.
            dp[day, HOLD] = max(dp[day - 1, HOLD], dp[day - 1, SELL] - stock_price)
            # If today we keep cash,
            # either we already kept cash yesterday, or we just sell out stock today
            dp[day, SELL] = max(dp[day - 1, SELL], dp[day - 1, HOLD] + stock_price)
        # To get maximal realized profit, final state must be SELL.
        last_day = len(prices) - 1
        return dp[last_day, SELL]

