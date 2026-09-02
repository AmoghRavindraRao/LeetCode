class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        i = 0
        j = 0
        
        while j < n and i < m:
            
            if t[j] == s[i]:
                i += 1
            
            j += 1
        
        return i == m
        