## we have an array of increasing numbers

## a target that we have to find 

## if it exist then return its index else return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0

        r = len(nums) - 1



        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                r = mid - 1
            
            elif nums[mid] < target:
                l = mid + 1
        
        return -1
            




        