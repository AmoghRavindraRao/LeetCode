# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        p = dummy = ListNode(0, head)

        for _ in range(left -1):
            p = p.next
        
        tail = p.next

        for _ in range(right - left):
            temp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = temp
        
        return dummy.next