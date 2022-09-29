from tkinter.tix import COLUMN


class Puzzle:

    def __init__ (self, size):
        self.size = size
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.findASafePlace(positions,0)


    def findASafePlace(self, positions, target_row):     
        if target_row == self.size:
            self.displayBoard(positions)

            # self.solutions +=1
        
        else:
            for col in range(self.size):

                if self.check_place(positions,target_row, col):
                    positions[target_row] = col
                    self.findASafePlace(positions, target_row + 1)


    def isSafe(self, positions, occupied_rows, col):
    
        for i in range(occupied_rows):
            if positions[i] == col or \
              positions[i] - i == col - occupied_rows or \
                positions[i] + i == col + occupied_rows:

                return False
        return True


    def placeQueen(board, i, j):
        board[i][j]=1


    def removeQueen(board, i, j):
        board[i][j]=0


    def displayBoard(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")







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

