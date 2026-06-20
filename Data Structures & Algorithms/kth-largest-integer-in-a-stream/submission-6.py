## find the kth largest values in a stream including duplicates

## so 3 is still technically the second largest because duplicates count 

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.heap = nums

        self.k = k
        
   

    def add(self, val: int) -> int:

        heapq.heappush(self.heap,val)
        heapq.heapify(self.heap)
        print(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[len(self.heap)-self.k]
            

        


        
