# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode()
        right_dummy = ListNode()

        left = left_dummy
        right = right_dummy

        while head is not None:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        right.next = None

        left.next = right_dummy.next

        return left_dummy.next