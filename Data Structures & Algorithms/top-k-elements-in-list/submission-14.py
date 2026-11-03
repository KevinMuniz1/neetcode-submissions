import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        freqHash = collections.Counter(nums)

        Heap = [(freq,num) for num,freq in freqHash.items()]

        heapq.heapify_max(Heap)

        for _ in range(k):
            res.append(heapq.heappop_max(Heap)[1])
        
        return res

        