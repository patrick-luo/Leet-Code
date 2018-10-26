# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda i:i.start)
        if len(intervals) < 2:
            return True
        for i, interv in enumerate(intervals[1:], 1):
            if interv.start < intervals[i-1].end:
                return False
        return True
