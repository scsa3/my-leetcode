from copy import deepcopy
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = list()
        for c in licensePlate:
            if c.isalpha():
                need += c.lower()
        result = str()
        for w in words:
            if result and len(w) >= len(result):
                continue
            clone = deepcopy(need)

            for c in w:
                try:
                    i = clone.index(c)
                except ValueError:
                    continue
                clone.pop(i)
                if len(clone) == 0:
                    result = w
                    continue
        return result


print(
    Solution().shortestCompletingWord('s', ["looks", "steps", "stripe", "stepple"])
)

# "1s3 PSt"
# ["step","steps","stripe","stepple"]
