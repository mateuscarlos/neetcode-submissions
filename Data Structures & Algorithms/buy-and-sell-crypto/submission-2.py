class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b, s = 0, 1

        while s < len(prices):
            if prices[s] < prices[b]:
                b = s
            else:
                curr_price = prices[s] - prices[b]
                profit = max((prices[s] - prices[b]), profit)
            
            s += 1

        return profit