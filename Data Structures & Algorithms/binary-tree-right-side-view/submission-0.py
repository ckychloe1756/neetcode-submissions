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
            rightside = None
            for i in range(num):
                node = heap.popleft()
                if node:
                    rightside = node
                    heap.append(node.left)
                    heap.append(node.right)
            if rightside:
                ans.append(rightside.val)
        return ans
                
                

            