class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = []
        res = []
        
        def solve(openB, closeB):
            if openB == closeB == n:
                res.append("".join(stk))
                return
            if openB<n:
                stk.append("(")
                solve(openB+1,closeB)
                stk.pop()
            if closeB<openB:
                stk.append(")")
                solve(openB, closeB+1)
                stk.pop()
        
        solve(0,0)
        return res