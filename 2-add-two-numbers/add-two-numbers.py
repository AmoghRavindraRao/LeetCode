# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """ 
        a = b = ""

        while l1:
            a = str(l1.val) + a
            l1 = l1.next

        while l2:
            b = str(l2.val) + b
            l2 = l2.next
        
        dummy = current = ListNode(0)

        for digit in str(int(a) + int(b))[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next