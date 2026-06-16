class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in s:
            if i == '*':
                result = result[:-1]
            elif i == '#':
                result = result + result
            elif i == '%':
                result = result[::-1]
            else:
                result += i
        return result