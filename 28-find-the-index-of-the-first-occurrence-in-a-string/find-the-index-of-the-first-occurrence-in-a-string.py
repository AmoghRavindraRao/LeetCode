class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        i = 0
        ans = -1
        if n == m and haystack == needle:
            return 0 
        while i + n <= m:
            if haystack[i: i + n] == needle:
                return i
            i += 1
        return ans
        