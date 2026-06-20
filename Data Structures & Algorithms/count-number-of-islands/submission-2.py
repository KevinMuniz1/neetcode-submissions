## go through the grid and if we find a 1 then we can see how deep we can go 
## we need to know which directions we can go 
## we need to know where we have been so we can store that in visited set
## maybe run a for loop through the grid and dfs when we find a one if its not arleady in visited
## once dfs is done then we can increment an island count 
## return numIslands 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        self.visited = set()
        
        numIslands = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col] == "1":

                    if (row,col) not in self.visited:
                        self.dfs(grid, row, col)
                        numIslands += 1
        
        return numIslands
                    

        
    def dfs(self, grid, row, col):

        
        if (row < 0 or row>= len(grid) or col < 0 or col >= len(grid[0])) or grid[row][col] == "0" or (row,col) in self.visited :
            return
        
        self.visited.add((row,col))
        

        directions = [(row + 1,col),(row - 1,col),(row,col + 1),(row,col - 1)]

        for direction in directions:
            self.dfs(grid,direction[0],direction[1])
    
        