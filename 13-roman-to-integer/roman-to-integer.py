class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            'I': 1,
            'V': 5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        n = len(s)
        arr = []
        for i in s:
            arr.append(data[i])
        ans = arr[-1]
        for i in range(n-2, -1,-1):
            if arr[i] < arr[i + 1]:
                ans -= arr[i]
            else:
                ans += arr[i]
        
        return ans
        