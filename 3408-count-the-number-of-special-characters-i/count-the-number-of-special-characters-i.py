class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = sorted(list(set(word)))
        count = 0
        for i in word:
            if i.isupper() and lower(i) in word:
                count += 1
        return count