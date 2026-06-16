class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = {}

        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i],0)
        
        return max(counter, key=counter.get)
        