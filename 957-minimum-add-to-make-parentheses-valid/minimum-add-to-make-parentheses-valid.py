class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(0)
            elif stack:
                temp = stack.pop()
                if temp != 0:
                    stack.append(temp)
                    stack.append(1)
            else:
                stack.append(1)
        
        return len(stack)