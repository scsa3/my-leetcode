from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        is_odd = False
        length = 0
        for v in c.values():
            if (v % 2) is 0:
                length += v
            else:
                is_odd = True
                length += (v - 1)
        if is_odd:
            length += 1
        return length
