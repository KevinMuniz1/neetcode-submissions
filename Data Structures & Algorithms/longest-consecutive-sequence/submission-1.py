class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        currCount = 0
        maxSubsequence = 0

        i = 0

        print(nums)

        if len(nums) == 0:
            return 0

        while i+1 < len(nums):
           
            if nums[i+1] - nums[i] == 1:
                currCount += 1
                if currCount > maxSubsequence:
                    maxSubsequence = currCount

            elif nums[i+1] - nums[i] == 0:
                i+=1
                continue
            else:
                currCount = 0
            i += 1
           
        return maxSubsequence + 1


        
        