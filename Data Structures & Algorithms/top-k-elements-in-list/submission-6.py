from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)

        res = []

        for i in range(len(nums)):
            counter[nums[i]] += 1
        
        heapItems = []

        for num in counter.keys():
            heapq.heappush(heapItems, (counter[num],num))
            if len(heapItems) > k:
                heapq.heappop(heapItems)
        
        print(heapItems)

        for nums in heapItems:
            res.append(nums[1])
        
        return res




        


        

            
        