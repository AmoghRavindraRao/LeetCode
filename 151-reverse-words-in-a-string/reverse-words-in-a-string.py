class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        ans = ' '.join(reversed(arr))
        return ans
        