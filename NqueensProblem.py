class Puzzle:

    def __init__ (self, size):
        '''Initializes the class and size of board and calls the solver function'''
        self.size = size

        self.solver()

    def solver(self):
        '''Creates empty solution array and ca```               ````````````````````````````                lls '''
        solutionArr = [0] * self.size
        self.findASafePlace(solutionArr,0)


    def findASafePlace(self, solutionArr, target_row):     
        if target_row == self.size:
            print(solutionArr)
            self.displayBoard(solutionArr)
            # self.printBoard(
            self.createBoard(solutionArr)
                # )
        
        else:
            for col in range(self.size):
                if self.isSafe(solutionArr,target_row, col):
                    solutionArr[target_row] = col
                    self.findASafePlace(solutionArr, target_row + 1)


    def isSafe(self, solutionArr, occupied_rows, col):
    
        for i in range(occupied_rows):
            if solutionArr[i] == col or \
              solutionArr[i] - i == col - occupied_rows or \
                solutionArr[i] + i == col + occupied_rows:
                return False
        return True


    def placeQueen(self, board, i, j):
        board[i][j]=1


    def removeQueen(self, board, i, j):
        board[i][j]=0


    def displayBoard(self, solutionArr):
        
        for row in range(self.size):
            line = ""
            for col in range(self.size):
                if solutionArr[row] == col:
                    line += "1 "
                else:
                    line += "0 "
            print(line)

        print("\n")


    def createBoard(self, solutionArr):
        board = []
        b = []

        for _ in range(self.size):
            b.append(0)

        for _ in range(self.size):
            board.append(b)

        for row in range(self.size):
            for col in range(self.size):
                if solutionArr[row] == col:
                    board[col][row] = 1
                else:
                    board[col][row] = 0
        
        # return board
        print(board)


    def printBoard(self, board):
        for i in range(self.size):
            for j in range(self.size):
                print(board[i][j], end = ' ')
            print()


    def main():
        N = int(input("What is the size of the board?"))
        Puzzle(N)


Puzzle.main()
