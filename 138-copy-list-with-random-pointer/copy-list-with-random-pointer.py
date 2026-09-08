"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        dummy = Node(0)
        curr = dummy
        original = head
        data = {}

        while original is not None:
            new = Node(original.val)
            curr.next = new
            curr = curr.next

            data[original] = new
            original = original.next

        original = head
        copied = dummy.next

        while original is not None:
            copied.random = (
                data[original.random]
                if original.random is not None
                else None
            )

            original = original.next
            copied = copied.next

        return dummy.next