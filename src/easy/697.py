from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_n = dict()
        count_n = dict()
        max_count = 0
        degree = 0
        for i, v in enumerate(nums):
            index = first_n.get(v)
            if index is None:
                first_n[v] = i
                count_n[v] = 1
            else:
                count_n[v] += 1

            if count_n[v] > max_count:
                degree = i - first_n[v] + 1
                max_count = count_n[v]
            elif count_n[v] == max_count:
                degree = min(degree, i - first_n[v] + 1)
        return degree


x = Solution().findShortestSubArray([1, 2, 2, 3, 1])
print(x)
