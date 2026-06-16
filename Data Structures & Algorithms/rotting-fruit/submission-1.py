from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([])
        count = 0
        fresh = 0
        mins = 0

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    count += 1
                if grid[i][j] == 1:
                    fresh += 1
        while q and fresh > 0:
            for _ in range(len(q)):            
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            mins += 1                           

            
        return mins if fresh == 0 else -1
               
        

        