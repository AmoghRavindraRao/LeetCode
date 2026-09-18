# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        from collections import deque

        if not root:
            return []

        q = deque([root])
        order = True
        result = []

        while q:
            lvl = len(q)
            arr = [0] * lvl

            for i in range(lvl):

                index = i if order else lvl - i - 1
                node = q.popleft()
                arr[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(arr)
            order = not order
        
        return result
        
        