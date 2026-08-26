class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        pre[0], suf[n - 1] = nums[0], nums[n-1]
        for i in range(1, n):
            pre[i] = nums[i] * pre[i - 1]
        
        for i in range(n - 2, -1, -1):
            suf[i] = nums[i] * suf[i + 1]
        ans = []
        ans.append(suf[1])
        for i in range(1,n - 1):
            ans.append(pre[i - 1] * suf[i + 1])
        ans.append(pre[-2])

        return ans

        