class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # use a hashmap to store the ending time and compare with other starting times
        # key = ending time, val = index of that interval in intervals
        # replace intervals --> working in-place

        sorted_intervals = sorted(intervals)
        res = [sorted_intervals[0]]

        for start, end in sorted_intervals:
            res_end = res[-1][1]
            if start <= res_end:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])

        return res
            
        