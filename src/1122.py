from collections import OrderedDict
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cache = OrderedDict()
        temp = []
        for i in arr2:
            cache[i] = []
        for i in arr1:
            if i in cache.keys():
                cache[i].append(i)
            else:
                temp.append(i)
        result = []
        for L in cache.values():
            result.extend(L)
        result.extend(sorted(temp))
        return result


