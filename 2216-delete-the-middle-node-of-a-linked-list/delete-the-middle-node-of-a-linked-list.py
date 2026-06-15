# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = fast = head
        if not head.next:
            return head.next

        while fast and fast.next:
            curr = slow
            slow = slow.next
            forward = slow.next
            fast = fast.next.next
        
        curr.next = forward
        return head
