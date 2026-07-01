class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()

        visited = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        level = 1

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        

        while q:

            for _ in range(len(q)):

                r,c = q.popleft()

                for row,col in directions:
                    nr, nc = r + row, c + col

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == -1 or ((nr,nc)) in visited:
                        continue
                    else:
                        grid[nr][nc] = level
                        q.append((nr,nc))
                        visited.add((nr,nc))

            level += 1
        
        






                





            

        