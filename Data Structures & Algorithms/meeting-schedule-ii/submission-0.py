"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort intervals by start time
        # keep an array of intervals <-- build ourselves
        # when we can't fit into any of the current days, then create new day
        # return len of the array

        intervals.sort(key=lambda i: i.start)

        days = []

        for interval in intervals:
            added = False
            for day in days:
                if day[-1].end <= interval.start:
                    day.append(interval)
                    added = True
                    break
            if not added:
                days.append([interval])

        return len(days)
        