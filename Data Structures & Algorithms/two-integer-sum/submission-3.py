class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp = {}

        for index, num in enumerate(nums):
            if target - num in comp:
                minimum = min(index, comp[target-num])
                maximum = max(index,comp[target-num])
                return [minimum,maximum]
            comp[num] = index
         
        