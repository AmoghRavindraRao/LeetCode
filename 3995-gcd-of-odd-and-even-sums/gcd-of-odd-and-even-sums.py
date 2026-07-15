class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        def get_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        return get_gcd(n*n, n*(n+1))