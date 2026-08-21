class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []

        for i in s:
            if i not in data:
                stack.append(i)
            else:
                if not stack or data[i] != stack.pop():
                    return False
        return len(stack) == 0

        