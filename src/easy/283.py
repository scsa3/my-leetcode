from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_indices = list()
        for i, v in enumerate(nums):
            if v == 0:
                zero_indices.append(i)
        count = len(zero_indices)
        for i in zero_indices[::-1]:
            nums.pop(i)

        nums.extend([0] * count)
