from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        for i in range(len(nums) + 1):
            result.extend(combinations(nums, i))
        return result
