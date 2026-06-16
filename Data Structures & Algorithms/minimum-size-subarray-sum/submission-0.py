class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0 

        currSum = 0

        minLen = float("inf")

        for R in range(len(nums)):

            currSum += nums[R]

            while currSum >= target:
                minLen = min(R - L + 1, minLen)
                currSum -= nums[L]
                L += 1


        return 0 if minLen == float("inf") else minLen



        