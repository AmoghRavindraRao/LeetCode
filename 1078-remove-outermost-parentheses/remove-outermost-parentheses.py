class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ''

        for i in s:
            if i == '(':
                if stack:
                    ans += i
                stack.append(i)
            else:
                if len(stack) != 1:
                    ans += i
                temp = stack.pop()
        
        return ans