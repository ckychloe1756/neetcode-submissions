class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pairs = {}
        count = 0
        for i in intervals:
            start = i[0]
            end = i[1]
            if start in pairs:
                pairs[start] = min(pairs[start],end)
                count += 1
            else:
                pairs[start] = end
        newpairs = dict(sorted(pairs.items()))
        
        end = newpairs[next(iter(newpairs))]
        count += -1
        for s in newpairs:
            if s < end:
                count += 1
                if newpairs[s] < end:
                    end = newpairs[s]
            else:
                end = newpairs[s]
            
        return count