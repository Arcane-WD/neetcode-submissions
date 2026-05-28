"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        intervals.sort(key = lambda i: i.start)
        start, end = intervals[0].start, intervals[0].end
        for interval in intervals[1:]:
            s,e = interval.start, interval.end
            if s<end:
                return False
            end = max(e,end)
        return True