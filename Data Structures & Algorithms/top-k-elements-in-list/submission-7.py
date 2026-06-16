## so we have a list and we want to get the k most elements that appear in list

## we can use the num as the key and count as value

## we can sort them  in order of count, then we pop those k times

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq = Counter(nums)

        res = []

        sortedFreq = sorted(freq.items(), key=lambda x: x[1])

        for _ in range(k):
            value = sortedFreq.pop()

            res.append(value[0])
        
        return res




        