## we are given an array of nums, find subarray with largest sum 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub = nums[0]

        currSum = 0


        for num in nums:

            if currSum < 0:
                currSum = 0

            currSum += num
            
            maxSub = max(currSum,maxSub)
        
        return maxSub
            



                



        