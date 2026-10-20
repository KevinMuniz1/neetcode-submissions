from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        countedNums = Counter(nums)

        countedNums = sorted(countedNums.items(), key=lambda item:item[1])

        return countedNums[-1][0]

        

         




        