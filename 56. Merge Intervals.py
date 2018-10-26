# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda i:i.start)
        merged = list()
        cur = intervals[0]
        for interv in intervals:
            if interv.start <= cur.end:
                cur.end = max(cur.end, interv.end)
            else:
                merged.append(cur)
                cur = interv
        merged.append(cur)
        return merged
