
b = [   [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
 
boardSize = len(b)



def printBoard (board):
    for i in range(boardSize):
        for j in range(boardSize):
            print(board[i][j], end = ' ')
        
        print()

def checkLastRow(board):
    for j in range(len(board)):
        if board[len(board)][j] == 1:
            return True
        
    return False

def clearBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j]=0


def checkValid(board, row, col):
    
    # Check if row is valid
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if column is valid
    for j in range(row):
        if board[j][col] == 1:
            return False
    
    # Check if left diagonal is valid
    for i, j in zip(range(row,-1, -1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    # Check if right diagonal (only left side) is valid
    for i, j in zip(range(row, boardSize, 1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve(board):
    for i in range(boardSize):
        for j in range(boardSize):
            if checkValid(board,i,j):
                board[i][j] = 1
                if i == boardSize:
                    printBoard(board)
                
            else:
                # clearBoard(board)
                printBoard(board)
        
        

solve(b)