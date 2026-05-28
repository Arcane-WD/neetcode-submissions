class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for tk in tokens:
            if tk in "+-/*":
                b,a = stk.pop(), stk.pop()
                if tk=="+":
                    stk.append(int(a)+int(b))
                elif tk == "-":
                    stk.append(int(a)-int(b))
                elif tk == "*":
                    stk.append(int(a)*int(b))
                else:
                    stk.append(int(a)/int(b))
            else:
                stk.append(tk)
        
        return int(stk[0])