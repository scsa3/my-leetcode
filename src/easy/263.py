class Solution:
    def isUgly(self, n: int) -> bool:
        if n is 0:
            return False
        while n % 2 is 0:
            n //= 2
        while n % 3 is 0:
            n //= 3
        while n % 5 is 0:
            n //= 5
        return n is 1
