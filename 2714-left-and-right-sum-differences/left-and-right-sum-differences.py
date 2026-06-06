class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        totalSum = sum(nums)
        leftSum = 0
        rightSum = 0
        ans = []
        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            ans.append(abs(rightSum - leftSum))
            leftSum = leftSum + nums[i]
        return ans