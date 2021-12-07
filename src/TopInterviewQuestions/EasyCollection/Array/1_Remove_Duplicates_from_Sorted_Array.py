from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        temp = None
        cache = []
        index = 0
        for n in nums:
            if n != temp:
                temp = n
                nums[index] = n
                index += 1
        for i, _ in enumerate(nums[index:]):
            nums[i + index] = "_"
        return index


x = [1, 1, 2]
y = Solution().removeDuplicates(x)
print(x, y)

for i, v in enumerate(range(10)[5:]):
    print(i)
