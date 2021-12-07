class Solution:
    def minPartitions(self, n: str) -> int:
        result = 1
        for i in n:
            x = int(i)
            if x == 9:
                return 9
            if x > result:
                result = x
        return result