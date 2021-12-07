from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        y = 0
        length = len(grid[0])
        for L in grid[::-1]:
            while y < length and L[y] >= 0:
                y += 1
            if y >= length:
                break
            result += (length - y)

        return result
