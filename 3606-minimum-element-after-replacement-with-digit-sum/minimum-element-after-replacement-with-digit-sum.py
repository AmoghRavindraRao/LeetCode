class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        for i in nums:
            s = str(i)
            temp = 0
            for j in s:
                temp += int(j)
            ans = min(ans, temp)


        
        return ans