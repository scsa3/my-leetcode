class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        reversed_list = [
            a_s[::-1] for a_s in s_list
        ]
        return " ".join(reversed_list)
