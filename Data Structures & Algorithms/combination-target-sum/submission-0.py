class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        stk = []
        res = []
        
        def solve(ind, stk, csum):
            if ind==len(nums):
                return
            if csum==target:
                if stk not in res:
                    res.append(stk.copy())
                return
            if nums[ind]>target-csum:
                return
            if csum<target:
                solve(ind+1,stk,csum)
                stk.append(nums[ind])
                solve(ind, stk, csum+nums[ind])
                solve(ind+1, stk, csum+nums[ind])
                stk.pop()
        
        solve(0,[],0)

        return res