"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mapping = defaultdict(int)
        for i in intervals:
            mapping[i.start] += 1
            mapping[i.end] -= 1
        cur_rooms = 0
        needed = 0
        for i in sorted(mapping.keys()):
            cur_rooms += mapping[i]
            needed = max(needed, cur_rooms)
        return needed