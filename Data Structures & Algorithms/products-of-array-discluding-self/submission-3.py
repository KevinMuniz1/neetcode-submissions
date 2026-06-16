class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):

            value = nums[i]
            nums.remove(nums[i])

            res.append(math.prod(nums))
            nums.insert(i,value)

        
        return res
