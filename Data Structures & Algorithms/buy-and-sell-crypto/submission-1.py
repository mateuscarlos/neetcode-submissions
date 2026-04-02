class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_price = 0
        b, s = 0, 1

        while s < len(prices):
            if prices[s] < prices[b]:
                b = s
            else:
                curr_price = prices[s] - prices[b]
            
            s += 1
            profit = max(curr_price, profit)

        return profit
            