class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))
        s.sort(reverse=True)
        return int(s[0]) * int(s[1])