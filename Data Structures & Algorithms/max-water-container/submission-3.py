class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                cand = min(heights[i],heights[j]) * (j - i)
                if cand > maxArea:
                    maxArea = cand
        
        return maxArea


            
        

        