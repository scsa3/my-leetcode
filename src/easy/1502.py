from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr.sort()
        diff = arr[1] - arr[0]
        for i, v in enumerate(arr[:-1]):
            if arr[i + 1] - v != diff:
                return False
        return True

