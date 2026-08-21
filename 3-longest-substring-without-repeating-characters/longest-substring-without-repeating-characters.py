class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        seen = {}

        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            
            length = max(length, right - left + 1)
            seen[c] = right

        return length
