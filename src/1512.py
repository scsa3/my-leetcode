from typing import List
from math import factorial


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        nums_map = dict()
        for i, v in enumerate(nums):
            map_v = nums_map.get(v, 0)
            map_v += 1
            nums_map[v] = map_v

        for i in nums_map.values():
            if i < 2:
                continue
            combination = factorial(i) // factorial(2) // factorial(i - 2)
            result += combination

        return result
