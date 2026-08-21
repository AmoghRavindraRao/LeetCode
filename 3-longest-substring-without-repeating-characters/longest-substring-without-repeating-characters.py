class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0

        for right, c in enumerate(s):
            if len(set(s[left:right + 1])) != right - left + 1:
                left += 1
            else:
                length = max(length, right - left + 1)
        
        return length
