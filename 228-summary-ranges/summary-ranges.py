class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        if n == 0:
            return []

        j = 0
        ans = []

        for i in range(1, n):
            if nums[i - 1] + 1 != nums[i]:
                if j == i - 1:
                    ans.append(str(nums[j]))
                else:
                    ans.append(str(nums[j]) + "->" + str(nums[i - 1]))

                j = i

        if j == n - 1:
            ans.append(str(nums[j]))
        else:
            ans.append(str(nums[j]) + "->" + str(nums[n - 1]))

        return ans