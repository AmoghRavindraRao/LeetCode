from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        data = {}

        for i in range(len(inorder)):
            data[inorder[i]] = i
        
        postorder = deque(postorder)

        def build(start, end):

            if start > end:
                return None
            
            root = TreeNode(postorder.pop())
            mid = data[root.val]
            
            root.right = build(mid + 1, end)
            root.left = build(start, mid - 1)

            return root
        
        root = build(0, len(inorder) - 1)

        return root