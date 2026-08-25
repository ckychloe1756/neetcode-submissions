class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = [intervals[0]]
        n = len(intervals)
        for start, end in intervals:
            if arr[-1][1] < start:
                arr.append([start, end])
            else:
                arr[-1][1] = max(arr[-1][1], end)
        return arr