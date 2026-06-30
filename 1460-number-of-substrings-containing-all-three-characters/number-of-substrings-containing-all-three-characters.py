class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {
            'a': -1,
            'b': -1,
            'c': -1
        }

        count = 0

        for i, ch in enumerate(s):
            last[ch] = i

            count += min(last.values()) + 1

        return count