## go through the grid and if we find a 1 then we can see how deep we can go 
## we need to know which directions we can go 
## we need to know where we have been so we can store that in visited set
## maybe run a for loop through the grid and dfs when we find a one if its not arleady in visited
## once dfs is done then we can increment an island count 
## return numIslands 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        islandCount = 0

        def dfs(r,c):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1" or (r,c) in visited:
                return
            
            visited.add((r,c))

            directions = [(r + 1,c),(r - 1,c),(r, c + 1),(r, c - 1)]

            for direction in directions:
                dfs(direction[0],direction[1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islandCount += 1
        
        return islandCount