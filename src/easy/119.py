from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        temp = [1, 1]
        result = []
        for _ in range(rowIndex - 1):
            for i in range(len(temp) - 1):
