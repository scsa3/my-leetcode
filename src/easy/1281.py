class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_n = 1
        sum_n = 0
        for c in str(n):
            i = int(c)
            product_n *= i
            sum_n += i
        return product_n - sum_n
