"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda r: r.start)
        k = 0
        for node in intervals:
            if k <= node.start:
                k = node.end
            else:
                return False
            
        return True