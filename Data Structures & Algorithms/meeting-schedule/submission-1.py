"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda t : t.start)
        prevend = 0
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start < prevend:
                return False
            prevend = end
        return True

