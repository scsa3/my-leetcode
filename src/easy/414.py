from typing import List
from math import inf


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        rank = [-inf, -inf, -inf]
        for n in nums:
            for i, v in enumerate(rank):
                if n == v:
                    break
                if n > v:
                    temp = rank[:i]
                    rank = rank[]
        return rank[-1]