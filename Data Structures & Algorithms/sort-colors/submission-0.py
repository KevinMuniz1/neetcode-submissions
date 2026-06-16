class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0,0,0]
        for i in range(len(nums)):
            if nums[i] == 0:
                counter[0] += 1
            elif nums[i] == 1:
                counter[1] += 1
            else:
                counter[2] += 1
        print(counter)
        i = 0
        for n in range(len(counter)):
            for j in range(0,counter[n]):
                nums[i] = n
                i += 1
        return nums 
        