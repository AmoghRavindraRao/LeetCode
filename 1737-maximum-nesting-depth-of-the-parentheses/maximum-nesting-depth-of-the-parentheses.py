class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0
        for i in s:
            if i == '(':
                count += 1
            if i == ')':
                count -= 1
            ans = max(ans, count)
        return ans