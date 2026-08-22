# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def path_sum(node):
            if not node:
                return 0
            left_max = path_sum(node.left)
            right_max = path_sum(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            res[0] = max(res[0], node.val + left_max + right_max)
            return node.val + max(left_max, right_max)
        path_sum(root)
        return res[0]
            