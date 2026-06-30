class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        
        ROWS, COLS = len(grid), len(grid[0])
        
        fresh = 0
        minutes = 0
        rottenQ = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rottenQ.append((r,c))


        while rottenQ and fresh > 0:

            for i in range(len(rottenQ)):
                r,c = rottenQ.popleft()

                directions = [(r + 1,c),(r - 1,c),(r, c + 1),(r, c - 1)]

                for direction in directions:
                    if direction[0] < 0 or direction[0] >= ROWS or direction[1] < 0 or direction[1] >= COLS or grid[direction[0]][direction[1]] == 0 or grid[direction[0]][direction[1]] == 2:
                        continue 
                    else:
                        grid[direction[0]][direction[1]] = 2
                        fresh -= 1
                        rottenQ.append((direction[0],direction[1]))
            minutes += 1
        

            
        if fresh > 0:
            return -1
        else:
            return minutes
            
        


                


        