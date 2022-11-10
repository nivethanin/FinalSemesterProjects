class GridMaker:
    '''Class to parse through the file and create the two dimensional array'''
    def gridMaker(gridFileName):
        grid = []
        S = 0
        #m is the size of the grid, was included separately in the text file

        with open(gridFileName,'r') as f:
            lines = f.readlines()
            S = int(lines[0])
            #first line contains the size of the grid

            for i in range(1,len(lines)):
                g = list(map(int, lines[i].split(' ')))
                grid.append(g)
                #adds the individual integers from each line in an array to the larger 2D array
            
        return grid, S
        #returns the 2D array and the size of the grid



class SudokuSolver:   
    def __init__(self, grid, S):
        ''' Initializes the class'''
        self.grid = grid
        self.S = S
    
    def printBoard(self):
        '''Prints the board'''
        for i in range(self.S):
            for j in range(self.S):
                print(self.grid[i][j],end = " ")
            print()
            
    def validPlacement(self, row, col, num):
        '''Checks to see if placement of a number is valid'''
        for x in range(self.S):
            if self.grid[row][x] == num:
                return False
                #Checks column if the 'num' number exists in it

        for x in range(self.S):
            if self.grid[x][col] == num:
                return False
                #Checks column if the 'num' number exists in it
    
        sectionRow = row - row % 3
        sectionCol = col - col % 3
        #Finds the top left coordinate of the 3x3 section that the placement is in

        for i in range(3):
            for j in range(3):
                if self.grid[i + sectionRow][j + sectionCol] == num:
                    return False
                    #Checks the placements 3x3 section already contains the 'num' number

        return True

    def solve(self):
        '''Calls the solver function'''
        self.solver(0,0)
        #Attempt to keep user code clean
    
    def solver(self, row, col):
        '''Recursive function that checks potential numbers for a position then
        makes recursive call for the next empty space (ignores existing numbers on the board)'''
    
        if (row == self.S - 1 and col == self.S):
            self.printBoard()
            return True
            #[Base case] if we get to final row and column then return true
            #The column index is equal to the max size because the calls to this function
            #increment the column

        if col == self.S:
            row += 1
            col = 0
            #Increment (go down one) row and reset column back to first column if column 
            #index is past max number

        if self.grid[row][col] > 0:
            return self.solver(row, col + 1)
            #Skips existing numbers in the grid

        for num in range(1, self.S + 1, 1): 
            if self.validPlacement(row, col, num):
                self.grid[row][col] = num
                #If the placement is a valid position for the number, place it
                if self.solver(row, col + 1):
                    return True
                    #Call the solve function on the next position
            self.grid[row][col] = 0
            #If valid placement isn't found set to zero
        return False
        #If no valid placements are found, return false
    

def main():
    gg, size = GridMaker.gridMaker('sudoku9TB.txt')
    s = SudokuSolver(gg, size)
    s.solve()

if __name__ == "__main__":
    main()
