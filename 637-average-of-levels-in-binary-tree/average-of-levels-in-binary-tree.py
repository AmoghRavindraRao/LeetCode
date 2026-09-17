# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []
        
        def solve(root, lvl):
            if root:
                if len(sums) == lvl:
                    sums.append(0)
                    count.append(0)

                sums[lvl] += root.val
                count[lvl] += 1
                solve(root.left, lvl + 1)
                solve(root.right, lvl + 1)
                return
        
        sums, count = [], []
        solve(root, 0)
        return [
            level_sum / count
            for level_sum, count in zip(sums, count)
        ]