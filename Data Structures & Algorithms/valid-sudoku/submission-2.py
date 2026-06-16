class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        if not self.bigSearch(board):
            return False
        

        for box_row in range(0, 9, 3):          
            for box_col in range(0, 9, 3):     
                if not self.smallSearch(board, box_row, box_col):
                    return False
        
        return True

    def bigSearch(self, board):
        for i in range(9):
            rowSeen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rowSeen:
                        return False
                    rowSeen.add(board[i][j])
        
        for i in range(9):
            colSeen = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in colSeen:
                        return False
                    colSeen.add(board[j][i])
        return True

    def smallSearch(self, board, startRow, startCol):
        seen = set()
        for i in range(3):
            for j in range(3):
                val = board[startRow + i][startCol + j]
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        return True
                