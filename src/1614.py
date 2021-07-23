class Solution:
    def maxDepth(self, s: str) -> int:
        left_count = 0
        result = 0
        for c in s:
            if c == '(':
                left_count += 1
                if left_count > result:
                    result = left_count
            elif c == ')':
                left_count -= 1
        return result
