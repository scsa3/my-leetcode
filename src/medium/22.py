from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = ["()"]
        

    @staticmethod
    def all(s_list: List[str]) -> List[str]:
        result = list()
        for s in s_list:
            new_s = f"({s})"
            result.append(new_s)
        return result

    @staticmethod
    def start_end(s_list: List[str]) -> List[str]:
        result = list()
        for s in s_list:
            start = f"(){s}"
            end = f"{s}()"
            result.append(start)
            result.append(end)
        return result
