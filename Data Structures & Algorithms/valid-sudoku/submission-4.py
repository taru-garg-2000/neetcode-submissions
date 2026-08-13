class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validateRows():
            for i in range(len(board)):
                rowSeen = set()
                for j in range(len(board[0])):
                    if board[i][j] != '.':
                        if board[i][j] not in rowSeen:
                            rowSeen.add(board[i][j])
                        else:
                            return False
            return True
        
        def validateColumns():
            for i in range(len(board[0])):
                colSeen = set()
                for j in range(len(board)):
                    if board[j][i] != '.':
                        if board[j][i] not in colSeen:
                            colSeen.add(board[j][i])
                        else:
                            return False   
            return True

        def validateBlocks():
            # Go over all the blocks
            for block in range(9):
                seen = set()
                start_row = (block // 3)*3
                start_col = (block % 3)*3
                for row in range(start_row, start_row+3):
                    for col in range(start_col, start_col+3):
                        if board[row][col] != '.':
                            if board[row][col] in seen:
                                return False
                            else:
                                seen.add(board[row][col])
            return True

        return validateRows() and validateColumns() and validateBlocks()