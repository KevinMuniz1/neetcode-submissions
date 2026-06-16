class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wantedNums = []
        for i in range(len(nums)):
            if nums[i] != val:
                print(nums[i])
                wantedNums.append(nums[i])
        nums[0:] = wantedNums
        return len(nums)


        
        