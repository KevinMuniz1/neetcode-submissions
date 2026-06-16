class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    canVal = self.foundIsland(grid, i, j)
                    if canVal > maxIslandCount:
                        maxIslandCount = canVal

        return maxIslandCount

    def foundIsland(self, grid, row, col) -> int:

        islandCount = 0

        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0

        if grid[row][col] == 1:

           grid[row][col] = 0
            
           return islandCount + 1 + self.foundIsland(grid,row + 1, col) + self.foundIsland(grid, row - 1, col) + self.foundIsland(grid,row, col - 1) + self.foundIsland(grid,row, col + 1)


        return islandCount
        