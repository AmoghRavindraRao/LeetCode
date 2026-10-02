class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def getParenthesis(open, close, s, n, res):
            if len(s) == 2 * n:
                res.append(s)

            if open < n:
                getParenthesis(open + 1, close, s + "(", n, res)

            if close < open:
                getParenthesis(open, close + 1, s + ")", n, res)
            
        res = []
        getParenthesis(0, 0, "", n, res)
        return res