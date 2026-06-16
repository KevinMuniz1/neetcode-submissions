class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        numSet = sorted(set(nums))
        nums[:len(nums)] = numSet
        return len(nums)
        

        