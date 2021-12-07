from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count: dict = Counter(chars)
        result = 0
        for a_word in words:
            w_count = Counter(a_word)
            flag = True
            for k, v in w_count.items():
                if count.get(k, 0) < v:
                    flag = False
                    break
            if flag:
                result += len(a_word)
        return result