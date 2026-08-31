class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [''] * numRows
        reverse = False
        i = 0
        n = len(s)

        while i < n:
            for down in range(numRows):
                if i < n:
                    arr[down] += s[i]
                    i += 1
            for up in range(numRows - 2, 0, -1):
                if i < n:
                    arr[up] += s[i]
                    i += 1
        
        ans = ''.join(arr)
        return ans



