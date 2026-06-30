## so we have a list and we want to get the k most elements that appear in list

## we can use the num as the key and count as value

## we can sort them  in order of count, then we pop those k times

## could solve it using bucket sort 

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countNums = Counter(nums)

        minHeap = [(cnt,value) for value,cnt in countNums.items()]

        res = []

        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        for item in minHeap:
            res.append(item[1])
        
        return res
        




        




        