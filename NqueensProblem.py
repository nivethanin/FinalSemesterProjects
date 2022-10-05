class Puzzle:

    def __init__ (self, size):
        '''Initializes the class and size of board and calls the solver function'''
        self.size = size

        self.solver()

    def solver(self):
        '''Creates empty solution array and calls find safe function'''
        solutionArr = [0] * self.size
        self.findASafePlace(solutionArr,0)


    def findASafePlace(self, solutionArr, currentRow):
        '''Recursive function that gets called each time a valid queen position is found
        and base case is when the queen on the final row is found, then prints the board'''     
        if currentRow == self.size:
            print(solutionArr)
            self.displayBoard(self.createBoard(solutionArr))
        
        else:
            for col in range(self.size):
                if self.isSafe(solutionArr,currentRow, col):
                    # iterates through each column and adds it to the solution array
                    # which is just a reference array with the coordinates for the solved boards
                    solutionArr[currentRow] = col
                    self.findASafePlace(solutionArr, currentRow + 1)


    def isSafe(self, solutionArr, completedRows, col):
        ''' Checks the position to see if there's any queens diagonals or on the same column'''
        for i in range(completedRows):
            if solutionArr[i] == col or \
              solutionArr[i] - i == col - completedRows or \
                solutionArr[i] + i == col + completedRows:
                return False
            #first line checks if there's a queen in the same colum
            #second line checks if theres a queen left up diagonal 
            #third line checks if theres a queen on the right up diagonal
        return True


    def placeQueen(self, board, i, j):
        board[i][j]=1


    def removeQueen(self, board, i, j):
        board[i][j]=0


    def createBoard(self, solutionArr):
        board =  [[0 for c in range(self.size)] for r in range(self.size)]

        for row in range(self.size):
            for col in range(self.size):
                if solutionArr[row] == col:
                    self.placeQueen(board,row,col)
                else:
                    self.removeQueen(board,row,col)
           
        return board
        


    def displayBoard(self, board):
        for i in range(self.size):
            for j in range(self.size):
                print(board[i][j], end = ' ')
            print()


    def main():
        N = int(input("What is the size of the board?"))
        Puzzle(N)


Puzzle.main()
