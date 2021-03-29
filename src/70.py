from math import factorial


class Solution:
    def climbStairs(self, n: int) -> int:
        one = n
        two = 0
        count = 0

        while one >= 0:
            result = factorial(one + two) // (factorial(one) * factorial(two))
            count += result
            one -= 2
            two += 1
        return count
