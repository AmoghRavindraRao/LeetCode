class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)

        divisor_count = [0] * (max_num + 1)
        divisor_sum = [0] * (max_num + 1)

        for d in range(1, max_num + 1):
            for multiple in range(d, max_num + 1, d):
                divisor_count[multiple] += 1
                divisor_sum[multiple] += d

        ans = 0
        for num in nums:
            if divisor_count[num] == 4:
                ans += divisor_sum[num]

        return ans