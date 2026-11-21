"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        rooms = []
        intervals.sort(key=lambda r: r.start)
        for obj in intervals:
            if rooms and rooms[0] <= obj.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, obj.end)

        return len(rooms)