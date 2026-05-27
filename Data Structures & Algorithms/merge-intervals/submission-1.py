class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervals = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            s,e = intervals[i]
            if s<=end:
                end = max(end, e)
            else:
                mergedIntervals.append([start, end])
                start, end = s,e
        if not mergedIntervals or mergedIntervals[-1]!=[start, end]:
            mergedIntervals.append([start, end])
        return mergedIntervals