from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        if sum(arr[-3:]) < target:
            return 0
        result = 0
        for i in range(len(arr)):
            left_index = i + 1
            right_index = len(arr) - 1
            while right_index > left_index:
                # print(i, left_index, right_index)

                head = arr[i]
                left = arr[left_index]
                right = arr[right_index]
                three_sum = sum([head, left, right])
                if three_sum > target:
                    right_index -= 1
                elif three_sum < target:
                    left_index += 1
                else:
                    fast_right_index = right_index
                    while arr[fast_right_index] == right and fast_right_index > left_index:
                        result += 1
                        # print('+1')
                        fast_right_index -= 1
                    left_index += 1

        return result


x = Solution().threeSumMulti([1, 1, 2, 2, 2, 2], 5)
print(x)

x = Solution().threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)
print(x)
