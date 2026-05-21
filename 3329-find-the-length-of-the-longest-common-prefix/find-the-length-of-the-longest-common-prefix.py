class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        data = set()
        max_len = 0
        for i in arr1:
            s = str(i)
            temp = ''
            for j in s:
                temp = temp + j
                data.add(temp)
        for i in arr2:
            s = str(i)
            temp = ''
            for j in s:
                temp += j
                if temp in data:
                    max_len = max(max_len, len(temp))
        return max_len