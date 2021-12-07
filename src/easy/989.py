from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        number = ''
        for i in A:
            number += str(i)
        number = int(number)
        number += K
        result = str(number)
        return [int(i) for i in result]
