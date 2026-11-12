class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 1:
            return intervals
        
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        

        for start,end in intervals[1:]:
            if res[-1][1] >= start:
                newStart = res[-1][0]
                newEnd = max(end,res[-1][1])
                res.pop()
                res.append([newStart,newEnd])
            else:
                res.append([start,end])
        return res

            

            


        
        