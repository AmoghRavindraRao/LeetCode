from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        if root is None:
            return 0
        ans = root.val

        def gain(node):

            nonlocal ans

            if node is None:
                return 0
            
            left = max(0, gain(node.left))
            right = max(0, gain(node.right))

            ans = max(ans, left + node.val + right)

            return node.val + max(left, right)
        
        gain(root)
        return ans
        
        return ans
            