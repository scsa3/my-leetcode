# https://leetcode.com/problems/fibonacci-number/discuss/308688/6-Python-solutions

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        x = 0
        y = 1

        for i in range(2, n + 1):
            x, y = y, x + y
        return y
