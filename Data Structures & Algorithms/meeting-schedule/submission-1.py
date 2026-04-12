"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the intervals based on the start time
        # check that the next start time is >= the current end time
        intervals.sort(key=lambda i: i.start)
        
        for i in range(len(intervals) - 1):
            if intervals[i + 1].start < intervals[i].end:
                return False

        return True
