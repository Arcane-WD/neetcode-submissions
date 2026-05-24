class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        ans=0
        for i in range(len(heights)+1):
            while stk and (i==len(heights) or heights[stk[-1]]>=heights[i]):
                height = heights[stk.pop()]
                width = i if not stk else i-stk[-1]-1
                ans = max(ans, height*width)
            stk.append(i)
        return ans