from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []
        
        q = deque([root])
        result = []
        
        def solve(node, lvl):
            if not node:
                return
            
            if len(result) == lvl:
                result.append([])
            
            result[lvl].append(node.val)
            solve(node.left, lvl + 1)
            solve(node.right, lvl + 1)
        
        solve(root, 0)
        return result