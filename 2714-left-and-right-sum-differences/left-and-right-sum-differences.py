class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)

        leftSum = [0] * (n)
        rightSum = [0] * (n)
        ans = [0] * (n)
        for i in range(1, n):
            leftSum[i] = nums[i-1] + leftSum[i-1]
        for i in range(n-2, -1, -1):
            rightSum[i] = nums[i+1] + rightSum[i+1]
        for i in range(0, n):
            ans[i] = abs(leftSum[i] - rightSum[i])
        
        return ans