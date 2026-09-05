class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        ans = []

        for i in arr:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(i)
        
        return '/' + '/'.join(ans)


        