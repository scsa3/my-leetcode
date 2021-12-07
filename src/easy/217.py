from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exist = set()
        for n in nums:
            if n in exist:
                return True
            exist.add(n)
        return False
