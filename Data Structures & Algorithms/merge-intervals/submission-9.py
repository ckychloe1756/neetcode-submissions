class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            prev_start, prev_end = arr[-1]
            start, end = intervals[i]
            if prev_end < start:
                arr.append(intervals[i])
                i += 1
            else:
                arr[-1][1] = max(prev_end, end)
                i += 1
        return arr