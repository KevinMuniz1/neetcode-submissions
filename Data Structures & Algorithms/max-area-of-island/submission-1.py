class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        ## get the len of both the rows and cols so we know where we need to go

        rLen = len(grid)

        cLen = len(grid[0])

        visited = set()

        maxIsland = 0

        def dfs(r,c):
              if r < 0 or r >= rLen or c < 0 or c >= cLen or grid[r][c] == 0 or (r, c) in visited:
                  return 0
              visited.add((r, c))
              return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(rLen):
            for c in range(cLen):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxIsland = max(dfs(r,c),maxIsland)
        
        return maxIsland

        

