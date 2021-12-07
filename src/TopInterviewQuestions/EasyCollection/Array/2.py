from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        low = prices[0]
        for v in prices[1:]:
            if v > low:
                profit += (v - low)
                low = v
            else:
                low = v
        return profit