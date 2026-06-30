import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        maxHeapData = [(sub[0]**2 + sub[1]**2,sub) for sub in points]

        res = []

        heapq.heapify_max(maxHeapData)

        print(maxHeapData)

        while len(maxHeapData) > k:
            heapq.heappop_max(maxHeapData)
        
        for dist, cord in maxHeapData:
            res.append(cord)
        
        return res