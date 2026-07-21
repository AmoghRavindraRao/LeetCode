class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = ['1']

        prev = s[0]
        pos = 0

        for inx, char in enumerate(s):
            if char != prev:
                arr.append(s[pos:inx])
                pos = inx
                prev = char

        arr.append(s[pos:])
        arr.append('1')
        output = 0
        for i in range(1,len(arr)-1):
            if '1' in arr[i] and '0' in arr[i-1] and '0' in arr[i+1]:
                    gain = len(arr[i-1]) + len(arr[i+1])
                    output = max(output, gain)
        
        return s.count('1') + output