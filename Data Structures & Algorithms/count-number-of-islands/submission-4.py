class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        ## go through the grid
        ## if we find a 1 then we can either dfs or bfs in order to keep looking for connected values of the island
        # we must also store a visited set so that we dont visit a part of the island twice
        # once we are done with visiting the whole island then we increment our island count and continue on with the grid

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islandCount = 0

        
        def dfs(grid,r,c):

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for ar,ac in directions:
                if r + ar < 0 or r + ar >= rows or c + ac < 0 or c + ac >= cols or (r+ar,c+ac)in visited or grid[r + ar][c + ac] == "0":
                    continue
                if grid[r + ar][c + ac] == "1":
                    visited.add((r+ar,c+ac))
                    dfs(grid,r+ar,c+ac)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    dfs(grid,r,c)
                    islandCount += 1
        
        return islandCount
        

