class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort()
        current_end = intervals[0][1]
        current_start = intervals[0][0]
        for start, end in intervals:
            if current_end < start:
                res.append([current_start, current_end])
                current_start = start
                current_end = end
            else:
                current_end = end if current_end <= end else current_end
        res.append([current_start, current_end])
        return res
