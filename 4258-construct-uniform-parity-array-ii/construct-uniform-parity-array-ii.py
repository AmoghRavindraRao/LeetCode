class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums1.sort()
        for i in range(1, n):
            if nums1[i] % 2 == nums1[0] % 2:
                continue
            else:
                temp = nums1[i] - nums1[0]
                if temp % 2 != nums1[0] % 2 or temp < 1:
                    return False
        
        return True