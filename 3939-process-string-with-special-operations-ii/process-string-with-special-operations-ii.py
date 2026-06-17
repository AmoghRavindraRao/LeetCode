class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        lengths = [0] * n
        curr = 0

        for j, i in enumerate(s):
            if i == '*':
                if curr > 0:
                    curr -= 1
            elif i == '#':
                curr *= 2
            elif i == '%':
                pass
            else:
                curr += 1
            lengths[j] = curr
        
        if k >= curr:
            return "."
        
        for i in range(n - 1, -1, -1):
            c = s[i]

            before = 0 if i == 0 else lengths[i - 1]
            after = lengths[i]

            if 'a' <= c <= 'z':
                if k == before:
                    return c
            elif c == '*':
                continue
            elif c == '#':
                if k >= before:
                    k -= before
            else:
                k = after - 1 - k

        return '.'        
       