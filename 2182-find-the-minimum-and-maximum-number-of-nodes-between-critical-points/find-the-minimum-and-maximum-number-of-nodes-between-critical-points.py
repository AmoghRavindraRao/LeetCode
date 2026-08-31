# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp = head

        data = []
        while temp != None:
            data.append(temp.val)
            temp = temp.next
        idx = []
        n = len(data)
        if n <= 2:
            return [-1, -1]
        for i in range(1, n - 1):
            if data[i-1] > data[i] and data[i + 1] > data[i]:
                idx.append(i)
            elif data[i-1] < data[i] and data[i + 1] < data[i]:
                idx.append(i)
        j = len(idx)
        if j < 2:
            return [-1, -1]
        maxi = idx[-1] - idx[0]
        mini = min(second - first for first, second in zip(idx, idx[1:]))

        return [mini, maxi]