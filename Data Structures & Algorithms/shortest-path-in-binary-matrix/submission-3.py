from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)])
        visit = set((0,0))

        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        while q:
            r , c , length = q.popleft()

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c]:
                continue
            
            if r == N - 1 and c == N - 1:
                return length
            
            for dr, dc in directions:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
                
        return -1 

