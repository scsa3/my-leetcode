class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num_str = str(num)
            num = sum(
                [int(c) for c in num_str]
            )
        return num
