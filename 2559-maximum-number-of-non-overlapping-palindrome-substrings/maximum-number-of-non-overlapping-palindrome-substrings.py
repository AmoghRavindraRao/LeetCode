class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        def pal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        ans = 0
        n = len(s)
        start = 0


        while start + k <= n:
            j = start + k

            if pal(start, j - 1):
                ans += 1
                start = j

            elif j < n and pal(start, j):
                ans += 1
                start = j + 1

            else:
                start += 1

        return ans

                
