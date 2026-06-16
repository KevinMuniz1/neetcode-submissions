import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                tempArray = nums[:i] + nums[i+1:]
                result.append(int(math.prod(tempArray)))
                tempArray = []
            else:
                result.append(int(math.prod(nums)/nums[i]))
        return result




            
        