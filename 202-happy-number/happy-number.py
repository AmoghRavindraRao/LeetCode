class Solution:
    def isHappy(self, n: int) -> bool:

        map = set()
        def pow(n):
            ans = 0

            while n:
                ans += (n % 10) ** 2
                n = n // 10
            
            return ans
        
        while n not in map:
            map.add(n)
            n = pow(n)

            if n == 1:
                return True
        
        return False