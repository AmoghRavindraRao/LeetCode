from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        q = deque([(root, 0)])
        ans = 0
        while q:
            node, number = q.pop()
            number = number * 10 + node.val

            if node.left is None and node.right is None:
                ans += number

            if node.left:
                q.append((node.left, number))
            if node.right:
                q.append((node.right, number))
            
        return ans