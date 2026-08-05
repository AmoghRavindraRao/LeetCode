class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = []
        i , j = 0, 1
        n = len(s)
        ans = 0
        while j <= n:
            flag = True
            if len(set(s[i:j])) == len(s[i:j]):
                flag = False
            if flag:
                i += 1
                j += 1
            else:
                ans = len(s[i:j])
                j +=1
        return ans
