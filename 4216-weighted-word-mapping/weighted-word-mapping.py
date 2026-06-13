class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        data = dict(zip(string.ascii_lowercase, weights))
        base_data = {letter: index for index, letter in enumerate(reversed(string.ascii_lowercase))}
        ans = ''
        for i in words:
            temp = 0
            for j in i:
                temp += data[j]
            temp = temp % 26
            ans += next(k for k, v in base_data.items() if v == temp)
        
        return ans
        
        

