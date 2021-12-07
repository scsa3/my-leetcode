class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_number = ""
        for c in s:
            n = ord(c) - 96
            s_number += str(n)
        result = 0
        for i in range(k):
            temp = 0
            for n in s_number:
                temp += int(n)
            result = temp
            s_number = str(result)
        return result


'''
Runtime: 36 ms, faster than 87.01% of Python3 online submissions for Sum of Digits of String After Convert.
Memory Usage: 14.3 MB, less than 28.22% of Python3 online submissions for Sum of Digits of String After Convert.
'''
