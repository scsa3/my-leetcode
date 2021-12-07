from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        revert_strs = zip(*strs)
        result = 0

        for s in revert_strs:
            origin_l = list(s)
            sorted_l = sorted(origin_l)
            if sorted_l != origin_l:
                result += 1
        return result


# s = "ab"
# s2 = "cd"
# x = zip(s, s2)
# print(list(x))
