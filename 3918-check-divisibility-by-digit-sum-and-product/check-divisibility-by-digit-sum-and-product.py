class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m = n
        s, p = 0, 1
        while m > 0:
            temp = m % 10
            m = m // 10
            s += temp
            p *= temp
        return (n % (s + p)) == 0
        