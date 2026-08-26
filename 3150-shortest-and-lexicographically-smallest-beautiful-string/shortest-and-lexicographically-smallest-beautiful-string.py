class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        one = 0
        ans = ""
        l = float("inf")

        def lexico(str1, str2):
            if not str1:
                return str2
            
            if len(str1) > len(str2):
                return str2
            
            if len(str2) > len(str1):
                return str1
            
            return min(str1, str2)
        
        for j in range(n):
            if s[j] == "1":
                one += 1
            while one == k:
                ans = lexico(ans, s[i:j + 1])
                
                if s[i] == "1":
                    one -= 1
                
                i += 1
        
        return ans


        
        return ans
        

        