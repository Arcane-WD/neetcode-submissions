class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n=len(nums)
        for i,a in enumerate(nums):
            if a>0:
                break
            
            if i>0 and a==nums[i-1]:
                continue

            j=i+1
            k=n-1
            while j<k:
                total = a+nums[j]+nums[k]
                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return ans