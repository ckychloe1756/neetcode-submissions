# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        heap = deque()
        heap.append(root)
        while heap:
            num = len(heap)
            level = []
            for i in range(num):
                node = heap.popleft()
                if node:
                    level.append(node.val)
                    heap.append(node.left)
                    heap.append(node.right)
            if level:
                ans.append(level)
        return ans