class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for num in nums:
            if num != val:
                k += 1
        
        i = 0
        for _ in range(k):
            while nums[i] == val:
                del nums[i]
            i += 1

        return k
        