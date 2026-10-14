class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        ## [int]
        ##return true if any value appears more than once

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
        ## return false otherwise