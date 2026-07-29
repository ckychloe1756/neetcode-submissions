# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node1 = head
        node2 = head
        while True:
            if not node1 or not node2 or not node1.next:
                return False
            node1 = node1.next.next 
            node2 = node2.next
            if node1 == node2:
                return True