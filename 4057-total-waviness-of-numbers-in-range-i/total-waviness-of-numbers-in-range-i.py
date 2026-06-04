class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def waviness(nums):
            nums = str(nums)
            n = len(nums)
            i = 2
            count = 0
            while i < n:
                if int(nums[i]) > int(nums[i - 1]) < int(nums[i - 2]):
                    count += 1
                elif int(nums[i]) < int(nums[i - 1]) > int(nums[i - 2]):
                    count += 1
                
                i += 1
            return count
        
        ans = 0
        for nums in range(num1, num2 + 1):
            temp = waviness(nums)
            ans += temp
        
        return ans