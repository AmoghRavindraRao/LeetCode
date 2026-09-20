class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, val in enumerate(s):
            ans = ans + (i + 1) * (ord('z') - ord(val) + 1)
        
        return ans