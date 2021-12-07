from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        exist = dict()
        for i, n in enumerate(nums):
            exist_index = exist.get(n)
            if exist_index is not None and ((i - exist_index) <= k):
                return True
            exist[n] = i
        return False


Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
