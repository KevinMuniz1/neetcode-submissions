class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setOfNums = set(nums)
        maximum = 1

        if not nums:
            return 0

        for num in nums:
            if num - 1 not in setOfNums:
                count = 1
                while num + 1 in setOfNums:
                    count += 1
                    num += 1
                    maximum = max(maximum,count)
        return maximum


        

        
        



        