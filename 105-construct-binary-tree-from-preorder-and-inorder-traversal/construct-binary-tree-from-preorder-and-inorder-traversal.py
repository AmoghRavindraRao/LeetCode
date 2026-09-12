from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        data = {}

        for i in range(len(inorder)):
            data[inorder[i]] = i
        
        preorder = deque(preorder)

        def build(start, end):
            if start > end:
                return None
            root = TreeNode(preorder.popleft())
            mid = data[root.val]

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            
            return root
        
        return build(0, len(inorder) - 1)