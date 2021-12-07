from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = list()
        for i, k in enumerate(nums):
            if i % 2 != 0:
                continue
            result.extend([nums[i + 1]] * k)
        return result
