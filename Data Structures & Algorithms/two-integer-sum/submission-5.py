class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp = {}

        for index,num in enumerate(nums):

            if target - num in comp and index != comp[target-num]:
                return [min(index,comp[target-num]),max(index,comp[target-num])]
            else:
                comp[num] = index
        


        