class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        while n != 0:
            temp = n % 10
            n = n // 10
            arr.append(temp)
        arr.sort(reverse=True)
        print(arr)
        return arr[0] * arr[1]