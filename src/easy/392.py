class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for c in t:
            if c == s[0]:
                s = s[1:]
                if len(s) == 0:
                    return True
        return False
