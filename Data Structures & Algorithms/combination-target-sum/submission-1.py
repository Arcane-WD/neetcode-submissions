class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def solve(ind, stk, csum):
            if csum==target:
                if stk not in res:
                    res.append(stk.copy())
                return
            if ind==len(nums) or csum>target:
                return
            stk.append(nums[ind])
            solve(ind,stk,csum+nums[ind])
            stk.pop()
            solve(ind+1, stk, csum)
        
        solve(0,[],0)

        return res