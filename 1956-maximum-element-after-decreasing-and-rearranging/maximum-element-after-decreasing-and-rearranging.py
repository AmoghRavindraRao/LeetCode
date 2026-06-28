class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        arr[0] = 1
        high = 1
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) > 1:
                arr[i] = arr[i - 1] + 1
            high = max(arr[i], arr[i - 1])
        
        return high
