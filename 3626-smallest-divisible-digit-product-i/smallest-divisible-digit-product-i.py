class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def product(n):
            p = 1
            if n == 0:
                return 0
            while n > 0:
                p *= n % 10
                n //= 10
            return p
        
        while product(n) % t != 0:
            n += 1
        
        return n