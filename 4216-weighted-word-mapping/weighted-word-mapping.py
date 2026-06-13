class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        # data = dict(zip(string.ascii_lowercase, weights))
        ans = ''
        for i in words:
            temp = 0
            for j in i:
                temp += weights[ord(j) - 97]
            temp = temp % 26
            index = 97 + 25 - temp
            ans += chr(index)
        return ans
        
        

