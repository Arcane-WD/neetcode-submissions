class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res+= [sorted(subset + [num]) for subset in res if sorted(subset+[num]) not in res]
        return res