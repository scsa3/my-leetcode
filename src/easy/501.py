from typing import List, Dict


# Not best
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        vals = self.get_val(root)
        counter = dict()
        max_count = 0
        result = set()
        for v in vals:
            count = counter.get(v, 0)
            count += 1
            counter[v] = count
            if count > max_count:
                max_count = count
                result = {v}
            if count == max_count:
                result.add(v)
        return list(result)

    def findMode2(self, root: TreeNode) -> List[int]:
        counter = self.get_val2(root)
        print(counter)
        max_count = 0
        result = set()
        for k, v in counter.items():
            if v > max_count:
                max_count = v
                result = {k}
            if v == max_count:
                result.add(k)
        return list(result)

    def get_val(self, root: TreeNode) -> List[int]:
        result = [root.val]
        if root.left:
            result.extend(
                self.get_val(root.left)
            )
        if root.right:
            result.extend(
                self.get_val(root.right)
            )
        return result

    def get_val2(self, root: TreeNode) -> Dict[int, int]:
        result = {
            root.val: 1
        }
        if root.left:
            left_result = self.get_val2(root.left)
            for k, v in left_result.items():
                count = result.get(k, 0)
                count += v
                result[k] = count

        if root.right:
            right_result = self.get_val2(root.right)
            for k, v in right_result.items():
                count = result.get(k, 0)
                count += v
                result[k] = count
        return result
