# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        while list1 is not None or list2 is not None:
            digit1 = list1.val if list1 is not None else 101
            digit2 = list2.val if list2 is not None else 101

            if digit1 <= digit2:
                nxt = ListNode(digit1)
                list1 = list1.next if list1 is not None else None
            else:
                nxt = ListNode(digit2)
                list2 = list2.next if list2 is not None else None
            
            curr.next = nxt
            curr = curr.next
        
        curr = curr.next
        return dummy.next