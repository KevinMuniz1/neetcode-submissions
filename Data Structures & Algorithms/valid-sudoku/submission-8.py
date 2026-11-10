from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowSeen = defaultdict(set)
        colSeen = defaultdict(set)
        square = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] in rowSeen[row] or board[row][col] in colSeen[col] or board[row][col] in square[(row//3,col//3)]:
                    return False
                if board[row][col] != ".":
                    rowSeen[row].add(board[row][col])
                    colSeen[col].add(board[row][col])
                    square[(row//3,col//3)].add(board[row][col])
        
        return True
        
        
        
        


