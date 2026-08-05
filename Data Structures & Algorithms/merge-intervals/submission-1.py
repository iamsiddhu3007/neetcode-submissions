class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda t:t[0])
        res = [intervals[0]]
        lastEnd = res[-1][-1]
        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            if start <= lastEnd:
                res[-1][-1] = max(end, lastEnd)
            else:
                res.append([start, end])
            lastEnd = res[-1][-1]
        return res



            
        