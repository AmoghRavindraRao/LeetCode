class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = {}
        i = 0
        ans = 0

        for j in range(len(nums)):
            frequency[nums[j]] = frequency.get(nums[j], 0) + 1
            while frequency[nums[j]] > k:
                frequency[nums[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans