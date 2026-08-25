class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr = []
        i = 0
        n = len(intervals)
        added = False

        while i < n:
            start, end = intervals[i]
            if end < newInterval[0] or (added and start > newInterval[1]):
                arr.append(intervals[i])
                i += 1
            else:
                if not added and start > newInterval[1]:
                    arr.append(newInterval)
                    added = True
                else:
                    newInterval[0] = min(start, newInterval[0])
                    newInterval[1] = max(end, newInterval[1])
                    i += 1
                    
        if not added:
            arr.append(newInterval)

        return arr