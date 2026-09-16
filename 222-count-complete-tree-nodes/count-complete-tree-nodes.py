from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:

        if not root:
            return 0

        def getDepth(node):
            if node is None:
                return 0
            return 1 + getDepth(node.left)
        
        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)