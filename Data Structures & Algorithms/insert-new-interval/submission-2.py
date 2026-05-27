class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.sort()

        result = []

        for i, cur in enumerate(intervals):

            if cur[1] < newInterval[0]:
                result.append(cur)
            elif cur[0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval[0] = min(cur[0], newInterval[0])
                newInterval[1] = max(cur[1], newInterval[1])

        result.append(newInterval)
        return result