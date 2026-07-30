# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # find the fist element of the second half part
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        # reverse the second half part
        prev = None
        slow.next = None # cut connection between halves
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # merge the two halves
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2


