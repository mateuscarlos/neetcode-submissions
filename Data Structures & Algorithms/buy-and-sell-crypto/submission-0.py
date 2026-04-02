class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_profit = 0
        l, r = 0, len(prices) - 1

        for i, v in enumerate(prices):
            while r > l:
                curr_profit = prices[r] - prices[l]
                if curr_profit < 0:
                    curr_profit = 0
                profit = max(profit, curr_profit)

                l += 1
                r -= 1
                
        return profit
                
