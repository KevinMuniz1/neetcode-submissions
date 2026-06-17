## rturn len of consec seq that can be formed 

## consec sequence in which element is exacly larger thatn the prev element

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)

        maxStreak = 0

        if len(nums) < 1:
            return 0

        for num in nums:

            currStreak = 0

            while num + 1 in setNums:
                currStreak += 1
                num = num + 1
                print("num",num)
            
            if currStreak > maxStreak:
                maxStreak = currStreak
        
        return maxStreak + 1



        