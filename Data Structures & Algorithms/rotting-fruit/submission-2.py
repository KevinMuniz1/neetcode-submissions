class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0

        time = 0

        rows = len(grid)

        cols = len(grid[0])

        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
   
        while fresh > 0 and q:

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1

            
                        
            
                

        


        


                