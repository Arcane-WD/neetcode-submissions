class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = []
        for i in range(len(temperatures)-1,-1,-1):
            # print([temperatures[i] for i in stk] if stk else [])
            while stk and temperatures[stk[-1]]<=temperatures[i]:
                stk.pop()
            if not stk:
                ans.append(0)
            else:
                ans.append(stk[-1]-i)
            stk.append(i)
        return ans[::-1]