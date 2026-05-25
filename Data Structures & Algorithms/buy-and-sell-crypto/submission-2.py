class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mprice=float('inf')
        ans = 0
        for i in prices:
            mprice = min(i, mprice)
            ans = max(ans, i-mprice)
        return ans