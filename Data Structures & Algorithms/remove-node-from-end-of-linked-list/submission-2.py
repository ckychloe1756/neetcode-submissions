# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nth_node = dummy
        head2 = dummy
        for _ in range(n):
            head2 = head2.next
        while head2 and head2.next:
            nth_node = nth_node.next
            head2 = head2.next
        nth_node.next = nth_node.next.next
        return dummy.next