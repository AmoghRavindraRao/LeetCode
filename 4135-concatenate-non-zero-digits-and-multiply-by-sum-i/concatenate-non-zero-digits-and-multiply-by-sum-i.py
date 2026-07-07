class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = '0'
        s = 0
        n = str(n)
        for i in n:
            if i != '0':
                x += i
                s += int(i)
        return int(x) * s