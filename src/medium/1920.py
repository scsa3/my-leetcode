from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = list()
        for i in nums:
            result.append(nums[i])
        return result