class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for i in range(n):
            j, k = i + 1, n-1
            while j < k:
                key = (nums[j], nums[i], nums[k])
                temp = nums[j] + nums[i] + nums[k]
                if temp == 0:
                    result.add(key)
                    j += 1
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    k -= 1
        ans = list(result)
        return ans