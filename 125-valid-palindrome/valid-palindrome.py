class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c for c in s if c.isalnum())
        s2 = s1.lower()
        return s2 == s2[::-1]