class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0

        last_count = 0
        now_char = s[0]
        now_count = 1
        result = 0

        for c in s[1:]:
            if c == now_char:
                now_count += 1
            else:
                last_count = now_count
                now_char = c
                now_count = 1
            if now_count <= last_count:
                result += 1

        return result
