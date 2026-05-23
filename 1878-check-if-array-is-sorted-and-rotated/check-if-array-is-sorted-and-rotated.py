class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        k, temp = 0, 150
        for i in range(n-1, -1, -1):
            if nums[i] <= temp:
                temp = nums[i]
                k = i
            else:
                break
        print(nums[k])      
        nums[:] = nums[k:] + nums[:k]
        print(nums)
        return nums == sorted(nums)

