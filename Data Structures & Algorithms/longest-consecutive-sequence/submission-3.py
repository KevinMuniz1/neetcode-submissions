## rturn len of consec seq that can be formed 

## consec sequence in which element is exacly larger thatn the prev element

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()

        print(nums )

        windowSize = 1

        maxWindow = 1

        if len(nums) < 1:
            return 0

        for i in range(len(nums)):

            if nums[i] == nums[i-1]:
                continue

            if nums[i] - nums[i-1] == 1:
                windowSize += 1
                if windowSize > maxWindow:
                    maxWindow = max(windowSize,maxWindow)
            else:
                if windowSize > maxWindow:
                    maxWindow = max(windowSize,maxWindow)
                windowSize = 1
        
        return maxWindow



        