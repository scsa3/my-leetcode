from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        result = list()
        for i, v in enumerate(numbers):
            if v > target:
                break
            while right > (i + 1) and (v + numbers[right]) > target:
                right -= 1

