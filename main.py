from Solver import Solver

sudoku = [
    [6, 0, 5, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 8, 0, 4, 6, 0, 0, 3, 0],
    [0, 4, 0, 3, 7, 0, 0, 6, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 7, 0, 0, 0, 2, 0, 0, 0],
    [1, 0, 0, 7, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 8, 0, 9, 0]
]

solver = Solver(sudoku)

if solver.solve():
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end="")
        print("")
else:
    print("No solution")