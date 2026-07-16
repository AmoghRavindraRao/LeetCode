class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        n = len(nums)
        mx = 0
        pregcd = []
        for i in nums:
            mx = max(mx, i)
            pregcd.append(gcd(i,mx))
        pregcd.sort()
        if n % 2 != 0:
            temp = n // 2
            del pregcd[temp]
            n -= 1
        i, j, s = 0, n-1, 0
        while i < j:
            s += gcd(pregcd[i], pregcd[j])
            i +=1
            j -= 1
        return s