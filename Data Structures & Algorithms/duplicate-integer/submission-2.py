class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) < len(nums) ## if equal then no value appears more than once

        