class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L = 0 
        R = len(heights) - 1

        maxArea = 0

        while L < R:
            cand = min(heights[L],heights[R]) * (R - L)
            if cand > maxArea:
                maxArea = cand
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maxArea


            
        

        