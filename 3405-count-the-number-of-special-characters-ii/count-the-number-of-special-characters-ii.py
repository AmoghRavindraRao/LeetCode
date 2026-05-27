
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        s = sorted(list(set(word)))
        count = 0
        for i in s:
            if i.isupper():
                U = i.upper()
                L = i.lower()
                if L in word and U in word and word.find(U) > word.rfind(L):
                    count += 1   
        return count        