from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a = [0] * n
        b = a * m

        for o in ops:
