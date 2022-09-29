class Puzzle:

    b = [   
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]


    def isSafe(board, row, col):
    
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
        for i, j in zip(range(row, len(board), 1), range(col,-1,-1)):
            if board[i][j] == 1:
                return False
        
        return True


    def placeQueen(board, i, j):
        board[i][j]=1


    def removeQueen(board, i, j):
        board[i][j]=0


    def displayBoard(board):
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j], end = ' ')
            print()


    def findASafePlace(board, row):     
        if row == len(board):
            board.displayBoard(board)

        for i in range(len(board)):
            if board.isSafe(board, row, i):
                board.placeQueen(board, row, i)

                board.findASafePlace(board, row+1)

                board.removeQueen(board, row, i)
            


N = input("What is the size of the board?")

createdBoard=[[ [0] * N for i in range(N)]]
solution = Puzzle()
solution.displayBoard(createdBoard)

