from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for banks in accounts:
            wealth = sum(banks)
            if wealth > result:
                result = wealth
        return result
