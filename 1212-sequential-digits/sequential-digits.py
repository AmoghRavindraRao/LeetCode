class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = '123456789'
        l = len(str(low))
        h = len(str(high))
        ans = []
        while l <= h:
            i = 0
            j = l
            while j <= 9:
                temp = int(s[i:j])
                if low <= temp <= high:
                    ans.append(temp)
                if temp > high:
                    break
                i += 1
                j += 1
            l += 1
        
        return ans