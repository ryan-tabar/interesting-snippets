# Store a board in an array or structure
# 'x' = not available
# 'o' = ball
# ' ' = empty

def printBoard(board):
    for row in board:
        print(row)

def copyBoard(board):
    return [[i for i in row] for row in board]

row_win = 3
col_win = 3
max_row = 7
max_col = 7

def doMoves(board, jumps_to_complete):

    if jumps_to_complete == 0 and board[row_win][col_win] == "o":
        return True

    for row in range(max_row):
        for col in range(max_col):
            if board[row][col] != "o":
                continue

            jump_overs = [
                [row - 1, col],
                [row + 1, col],
                [row, col - 1],
                [row, col + 1],
            ]
            jump_tos = [[row - 2, col], [row + 2, col], [row, col - 2], [row, col + 2]]

            for i, jump in enumerate(jump_tos):
                boardCopy = copyBoard(board)

                jump_to_row = jump[0]
                jump_to_col = jump[1]
                jump_over_row = jump_overs[i][0]
                jump_over_col = jump_overs[i][1]
                try: 
                    if ( boardCopy[jump_over_row][jump_over_col] == "o"
                    and boardCopy[jump_to_row][jump_to_col] == " "):
                        # make the jump
                        boardCopy[row][col] == " "
                        boardCopy[jump_to_row][jump_to_col] = "o"
                        boardCopy[jump_over_row][jump_over_col] = " "
                        if doMoves(boardCopy, jumps_to_complete - 1):
                            printBoard(boardCopy)
                            return True
                except IndexError:
                    pass
    return False

test_board = [
    ["x", "x", "o", "o", "o", "x", "x"],
    ["x", "x", "o", "o", "o", "x", "x"],
    ["o", "o", "o", "o", "o", "o", "o"],
    ["o", "o", "o", " ", "o", "o", "o"],
    ["o", "o", "o", "o", "o", "o", "o"],
    ["x", "x", "o", "o", "o", "x", "x"],
    ["x", "x", "o", "o", "o", "x", "x"],]

doMoves(test_board, 31)

# 	bool doMoves( board )

# 		check if this is a winning position
# 			return true!

# 		for every piece on the board
# 			for every direction you can move
# 				make a copy of the board
# 				make the move on the copy
# 				if (doMoves( copy))
# 					print the copy
# 					return true

# 		return false;
