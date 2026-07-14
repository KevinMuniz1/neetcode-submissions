from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowSet = defaultdict(set)

        colSet = defaultdict(set)

        smallSquare = defaultdict(set)

        for r in range(9):
            for c in range(9):

                grid = board[r][c]


                if grid == ".":
                    continue

                if grid in rowSet[r] or grid in colSet[c] or grid in smallSquare[(r//3,c//3)]:
                    return False

                rowSet[r].add(grid)
                colSet[c].add(grid)
                smallSquare[(r//3,c//3)].add(grid)
        
        return True

