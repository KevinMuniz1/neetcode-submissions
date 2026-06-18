##we are given an integer array where each val is the height of the bar 

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxWater = float('-inf')

        l = 0

        r = len(heights) - 1

        while l < r:

            currMaxWater = (min(heights[l], heights[r]) * (r-l))

            maxWater = max(maxWater,currMaxWater )

            print("left p",heights[l],l,end="")
            print("right p",heights[r],r)

            if heights[l] > heights[r]:
                r-=1
                continue
            
            if heights[r] > heights[l]:
                l += 1
                continue
            
            if heights[r] == heights[l]:
                l += 1
                r -= 1
                        
        
        return maxWater

        


        