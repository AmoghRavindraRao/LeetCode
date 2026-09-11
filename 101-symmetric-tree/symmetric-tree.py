# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        dummy = root

        stack = [(dummy, root)]

        while stack:

            n1, n2 = stack.pop()

            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False

            stack.append([n1.left, n2.right])
            stack.append([n1.right, n2.left])
        
        return True