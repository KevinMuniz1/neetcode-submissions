class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## we can compare the area as a whole and return biggest area
        maxArea = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                temp = min(heights[i], heights[j])
                if temp * (j - i) > maxArea:
                    maxArea = temp * (j- i)
        return maxArea

      


        