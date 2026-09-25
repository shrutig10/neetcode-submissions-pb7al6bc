class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # sorted, non overlapping
        # new interval is completely before the next interval
        # add new interval and then return the rest
        # new interval is completely after the next interval
        # add next
        # new interval is overlapping with the next interval
        # update interval such that i take the min start and max end
        

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res
