class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)

        maxNum = 0

        for num in numSet:

            currNum = num

            if (num - 1) not in numSet:
                count = 1

                while currNum + 1 in numSet:

                    count += 1
                    currNum += 1
            
                maxNum = max(maxNum,count)
        
        return maxNum
            
        