class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islandCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islandCount += 1
                    self.foundIsland(grid, i, j)


        return islandCount

    
    def foundIsland(self,grid, row, col):

        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] == "1":

            grid[row][col] = "0" 

            self.foundIsland(grid, row + 1, col) ## up

            self.foundIsland(grid, row - 1, col) ## down

            self.foundIsland(grid, row, col + 1) ## right

            self.foundIsland(grid, row, col - 1) ## left
        

        

