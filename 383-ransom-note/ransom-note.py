from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = dict(Counter(ransomNote))
        b = dict(Counter(magazine))

        for i, j in a.items():
            if i not in b or b[i] < j:
                return False

        return True 
        