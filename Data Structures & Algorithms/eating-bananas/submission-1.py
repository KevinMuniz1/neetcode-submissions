class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        best = float("inf")

        l = 1
        r = max(piles)

        while l <= r:
            testRate = l + (r - l) // 2

            hourCount = 0

            for num in piles:
                hourCount += (num + testRate - 1) // testRate

            if hourCount > h:
                l = testRate + 1
            else:
                best = min(best,testRate)
                r = testRate - 1

        return best