class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        prod = 1
        for i in nums:
            if i==0:
                zeros+=1
            else:
                prod*=i
        for i in range(len(nums)):
            if nums[i]==0:
                if zeros==1:
                    nums[i]=prod
                else:
                    nums[i]=0
            else:
                if zeros>0:
                    nums[i]=0
                else:
                    nums[i] = prod//nums[i]
        return nums