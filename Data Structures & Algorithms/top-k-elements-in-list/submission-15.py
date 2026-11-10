import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        heapify_list = [(value,key) for key,value in freq.items()]

        heapq.heapify(heapify_list)

        while len(heapify_list) > k:
            heapq.heappop(heapify_list)
        
        return [value for key,value in heapify_list]



        

        








        