class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp = {}

        for index,value in enumerate(nums):
            if (target - value) in comp:
                return [comp[target-value],index]
            else:
                comp[value] = index
                


        