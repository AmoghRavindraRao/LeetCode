class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = sorted(abs(x) for x in nums)
        ans = 0
        temp = True
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if temp:
                ans += arr[-1] ** 2
                _ = arr.pop(-1) 
                temp = not temp
            else:
                ans -= arr[0] ** 2
                _ = arr.pop(0)
                temp = not temp
        return ans
        