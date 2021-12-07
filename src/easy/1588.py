from itertools import combinations
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        weight = [0] * length
        # for

    def foo(self, numbers: List[int], times: int) -> list:
        down_index = len(numbers) - times
        if times > len(numbers) // 2:
            down_index = len(numbers) // 2
        result = []
        v = 0
        for i in range(len(numbers)):
            if i < times:
                v += 1
            elif i > down_index:
                v -= 1
            result.append(v)
        return result


if __name__ == '__main__':
    x = Solution().foo([1, 2, 3, 4], 3)
    print(x)
