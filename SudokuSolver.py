class GridMaker:
    def gridMaker(gridFileName):
        grid = []
        m = 0

        with open(gridFileName,'r') as f:
            lines = f.readlines()
            M = int(lines[0])

            for i in range(1,len(lines)):
                g = list(map(int, lines[i].split(' ')))
                grid.append(g)
                
        return grid, m



class SudokuSolver:   
    def __init__(self, grid, M):
        self.grid = grid
        self.M = M
    
    def puzzle(self):
        for i in range(self.M):
            for j in range(self.M):
                print(self.grid[i][j],end = " ")
            print()
            
    def solve(self, row, col, num):
        for x in range(self.M):
            if self.grid[row][x] == num:
                return False
                
        for x in range(self.M):
            if self.grid[x][col] == num:
                return False
    
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + startRow][j + startCol] == num:
                    return False
        return True
    
    def Suduko(self, row, col):
    
        if (row == self.M - 1 and col == self.M):
            return True
        if col == self.M:
            row += 1
            col = 0
        if self.grid[row][col] > 0:
            return self.Suduko(row, col + 1)
        for num in range(1, self.M + 1, 1): 
        
            if self.solve(row, col, num):
            
                self.grid[row][col] = num
                if self.Suduko(row, col + 1):
                    return True
            self.grid[row][col] = 0
        return False
    

gg, size = GridMaker.gridMaker('sudoku9TB.txt')
grid = [[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]]
s = SudokuSolver(grid, size)

# print(gg)

if (s.Suduko(0, 0)):
    s.puzzle()
else:
    print("No Solution!!!!")


M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''
grid = [[0, 0, 3, 0, 2, 0, 6, 0, 0], [9, 0, 0, 3, 0, 5, 0, 0, 1], [0, 0, 1, 8, 0, 6, 4, 0, 0], [0, 0, 8, 1, 0, 2, 9, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 6, 7, 0, 8, 2, 0, 0], [0, 0, 2, 6, 0, 9, 5, 0, 0], [8, 0, 0, 2, 0, 3, 0, 0, 9], [0, 0, 5, 0, 1, 0, 3, 0, 0]]
 
# if (Suduko(grid, 0, 0)):
#     puzzle(grid)
# else:
#     print("Solution does not exist:(")