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
            mapping[i.start]+=1
            mapping[i.end]-=1
        prev = 0
        res = 0
        for i in sorted(mapping.keys()):
            prev += mapping[i]
            res = max(res, prev)
        return res