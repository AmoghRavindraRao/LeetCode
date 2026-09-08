# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        n = 0
        curr = head
        while curr is not None:
            n += 1
            curr = curr.next
        
        k %= n

        if k == 0:
            return head
        
        left = head
        right  = head

        for _ in range(k):
            right = right.next

        while right.next is not None:
            right = right.next
            left = left.next
        
        new_head = left.next
        left.next = None
        right.next = head
        return new_head