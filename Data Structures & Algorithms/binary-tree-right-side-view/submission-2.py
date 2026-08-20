# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        heap = deque()
        ans = []
        heap.append(root)
        while heap:
            num = len(heap)
            for i in range(num):
                node = heap.popleft()
                if node.left:
                    heap.append(node.left)
                if node.right:
                    heap.append(node.right)
            ans.append(node.val)
        return ans
