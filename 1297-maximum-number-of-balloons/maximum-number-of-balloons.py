class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        data = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }

        for i in text:
            if i in data:
                data[i] += 1
        data['l'] = data['l'] // 2
        data['o'] = data['o'] // 2
        return min(data.values())
