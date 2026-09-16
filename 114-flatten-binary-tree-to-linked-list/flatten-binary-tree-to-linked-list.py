from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        q = deque([root])
        ans = TreeNode(-999)
        dummy = ans
        while q:

            node = q.pop()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            
            dummy.right = node
            dummy.left = None
            dummy = node
        
        dummy.left = None
        dummy.right = None
        
        return ans.right