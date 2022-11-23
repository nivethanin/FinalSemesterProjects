

class Puzzle:

    board = [0][0]
    Size = len

    def isSafe(board, row, col):
    
        # Check if row is valid
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check if column is valid
        # for j in range(row):
        #     if board[j][col] == 1:
        #         return False
        
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


    def findASafePlace(board, col):     
        if col>= len(board):
            Puzzle.displayBoard(board)
            return True


        for i in range(len(board)):
            if Puzzle.isSafe(board, i, col):
                Puzzle.placeQueen(board, i, col)

                if Puzzle.findASafePlace(board, col+1)==True:
                    return True

                Puzzle.removeQueen(board, i, col)
        
        return False




N = int(input("What is the size of the board?"))
a = []
b = []

for j in range(0, N):
        b.append(0)

for i in range(0, N):
    a.append(b)

createdBoard=a

solution = Puzzle()
solution.board = createdBoard

Puzzle.displayBoard(createdBoard)
solution.findASafePlace(0)
if solution.findASafePlace(solution.board,0)==False:
    print("No solution possible")

