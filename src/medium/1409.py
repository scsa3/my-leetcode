from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))
        result = []
        for i in queries:
            index = p.index(i)
            j = p.pop(index)
            result.append(index)
            p.insert(0, j)
        return result


if __name__ == '__main__':
    x = Solution().processQueries(
        [3, 1, 2, 1],
        5,
    )
    print(x)
