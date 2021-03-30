from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = 2_000_001
        result = list()
        for i, v in enumerate(arr[:-1]):
            next_v = arr[i + 1]
            diff = next_v - v
            if diff < minimum:
                minimum = diff
                result = [[v, next_v]]
            elif diff == minimum:
                result.append([v, next_v])
        return result
