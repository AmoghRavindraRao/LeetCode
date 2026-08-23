class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        res = 0
        for i in range(n):
            if i < n // 2:
                sign = 1
            else:
                sign = -1
            
            if num[i] == '?':
                value = 4.5
            else:
                value = int(num[i])
            
            res += sign * value
        
        return not res == 0
        