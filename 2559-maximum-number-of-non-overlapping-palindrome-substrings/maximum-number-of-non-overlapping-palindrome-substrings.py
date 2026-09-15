class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        def pal(s):
            return s == s[::-1]
        ans = 0
        n = len(s)
        start = 0


        while start + k <= n:
            j = start + k

            if pal(s[start:j]):
                ans += 1
                start = j

            elif j < n and pal(s[start: j + 1]):
                ans += 1
                start = j + 1

            else:
                start += 1

        return ans

                
