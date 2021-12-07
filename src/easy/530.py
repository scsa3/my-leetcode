import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.numbers = []
        self.collect_val(root)
        self.numbers.sort()
        min_diff = math.inf
        for i, v in enumerate(self.numbers[:-1]):
            diff = self.numbers[i + 1] - v
            if diff < min_diff:
                min_diff = diff
                if min_diff == 0:
                    return 0

        return min_diff

    def collect_val(self, node: TreeNode):
        self.numbers.append(node.val)

        if node.left:
            self.collect_val(node.left)

        if node.right:
            self.collect_val(node.right)
