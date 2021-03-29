from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        less_map = dict()
        for y in nums[1:-1]:
            for z in nums[2:]:
                yz_sum = y + z
                temp = less_map.get(yz_sum, list())
                if [y, z] not in temp:
                    temp.append([y, z])
                    less_map[yz_sum] = temp
        for x in nums[]
