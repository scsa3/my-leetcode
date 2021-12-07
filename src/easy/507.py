import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        divisor_half = math.sqrt(num)
        divisor_half = int(divisor_half)
        divisors_sum = 1
        for i in range(2, divisor_half + 1):
            remainder = num % i
            if remainder == 0:
                divisors_sum += i
                divisors_sum += num // i
        return divisors_sum == num


x = Solution().checkPerfectNumber(2)
print(x)
