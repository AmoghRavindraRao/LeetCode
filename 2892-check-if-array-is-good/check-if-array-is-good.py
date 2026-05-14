import numpy as np
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_n = max(nums)
        u = len(np.unique(nums))
        if (max_n + 1 != n) or (u != max_n):
            return False
        count = nums.count(max_n)
        if count == 2:
            return True
        else:
            return False