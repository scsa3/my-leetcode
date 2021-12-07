from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, v in enumerate(words):
            for j, w in enumerate(words):
                if i == j:
                    continue
                if v in w:
                    result.append(v)
                    break
        return result
