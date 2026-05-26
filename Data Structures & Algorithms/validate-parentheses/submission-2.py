class Solution:
    def isValid(self, s: str) -> bool:
        prens = {")":"(", "]":"[", "}":"{"}
        stk = []
        for i in s:
            if i not in prens.keys():
                stk.append(i)
                # print(stk)
            else:
                if not stk:
                    return False
                else:
                    if stk[-1]==prens[i]:
                        stk.pop()
                    else:
                        return False
        if not stk:
            return True
        return False