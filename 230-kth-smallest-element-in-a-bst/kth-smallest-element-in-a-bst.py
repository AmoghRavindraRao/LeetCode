# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count =0
        self.ans = 0

        def solve(node):

            if not node:
                return
            solve(node.left)

            self.count += 1
            if self.count == k:
                self.ans = node.val
                return
            
            if self.count < k:
                solve(node.right)
            
        solve(root)
        return self.ans
