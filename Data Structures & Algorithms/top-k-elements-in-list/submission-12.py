import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqHash = collections.Counter(nums)


        minHeap = [(freq,num) for num,freq in freqHash.items()]

        heapq.heapify(minHeap)


        while len(minHeap) > k:
            heapq.heappop(minHeap)
            
        return [num[1] for num in minHeap]