class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # use a hashmap to store the ending time and compare with other starting times
        # key = ending time, val = index of that interval in intervals
        # replace intervals --> working in-place

        sorted_intervals = sorted(intervals)
        res = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            res_idx = len(res) - 1
            if sorted_intervals[i][0] <= res[res_idx][1]:
                res[res_idx][0] = min(sorted_intervals[i][0], res[res_idx][0])
                res[res_idx][1] = max(sorted_intervals[i][1], res[res_idx][1])
            else:
                res.append(sorted_intervals[i])

        return res
            
        