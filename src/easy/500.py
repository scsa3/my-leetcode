from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = list()

        for i, w in enumerate(words):
            print(type(w))
            w = w.lower()
            is_row1 = True
            is_row2 = True
            is_row3 = True

            for c in w:
                if is_row1 and c not in row1:
                    is_row1 = False
                if is_row2 and c not in row2:
                    is_row2 = False
                if is_row3 and c not in row3:
                    is_row3 = False
                if not any([is_row1, is_row2, is_row3]):
                    break
            if any([is_row1, is_row2, is_row3]):
                result.append(words[i])
        return result


x = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
print(x)
