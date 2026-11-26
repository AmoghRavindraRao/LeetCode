class Solution:
    def canAliceWin(self, n: int) -> bool:
        r=10
        while(n>=r):
            n-=r
            r-=1
            if n>=r:
                n-=r
                r-=1
            else:
                return True
        return False        