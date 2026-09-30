class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = []
        for i in seq:
            if i == '(':
                ans.append(depth % 2)
                depth += 1
            if i == ')':
                depth -= 1
                ans.append(depth % 2)
        
        return ans