class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return sorted(nums)==list(range(1,len(nums)))+[len(nums)-1]