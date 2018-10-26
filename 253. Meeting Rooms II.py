# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda i:i.start)
        rooms = list()
        for i, interv in enumerate(intervals):
            settled = False
            for m, meeting in enumerate(rooms):
                if meeting.end <= interv.start:
                    rooms[m] = interv
                    settled = True
                    break
            if not settled:    
                rooms.append(interv)
        return len(rooms)                
                    
                        
