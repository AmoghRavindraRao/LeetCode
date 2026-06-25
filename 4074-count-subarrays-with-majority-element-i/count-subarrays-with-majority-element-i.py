class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n, ans = len(nums), 0

        for i in range(n):
            cnt = 0

            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1

                if 2 * cnt > j - i + 1:
                    ans += 1

        return ans        