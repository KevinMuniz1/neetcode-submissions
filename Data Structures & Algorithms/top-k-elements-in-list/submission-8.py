## so we have a list and we want to get the k most elements that appear in list

## we can use the num as the key and count as value

## we can sort them  in order of count, then we pop those k times

## could solve it using bucket sort 

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        freq = [[] for i in range(len(nums) + 1)]

        for num, count in counter.items():
            freq[count].append(num)
        
        res = []
        
        for arr in freq[::-1]:
            for num in arr:
                res.append(num)
            if len(res) == k:
                return res
        




        




        