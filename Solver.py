
'''
@author Gerardo Guerrero <gguerr21@itam.mx>
Jun 18, 2023

based on the Sudoku Solver
implemented by Coding with John
https://www.youtube.com/watch?v=mcXc8Mva2bA
'''
class Solver:
    SIZE = 9

    def __init__(self, board):
        self.board = board

    def __check_row(self, i, num):
        # Checks if the given number exists in the i row
        return self.__check_row_recursive(0, i, num)

    def __check_row_recursive(self, index, i, num):
        # Recursive function to check if the given number exists in the i row
        if self.board[i][index] == num:
            return True
        elif index < self.SIZE - 1:
            return self.__check_row_recursive(index + 1, i, num)
        else:
            return False

    def __check_column(self, j, num):
        # Checks if the given number exists in the j column
        return self.__check_column_recursive(0, j, num)

    def __check_column_recursive(self, index, j, num):
        # Recursive function to check if the given number exists in the j column
        if self.board[index][j] == num:
            return True
        elif index < self.SIZE - 1:
            return self.__check_column_recursive(index + 1, j, num)
        else:
            return False

    def __check_inner_box(self, i, j, num):
        # Check if the given number exists in the 3x3 inner box containing the specified cell
        row = i - i % 3
        column = j - j % 3

        for k in range(row, row + 3):
            for l in range(column, column + 3):
                if self.board[k][l] == num:
                    return True
        return False

    def __check_num(self, i, j, num):
        # Check if the given number can be placed in the specified cell
        return (
            not self.__check_row(i, num)
            and not self.__check_column(j, num)
            and not self.__check_inner_box(i, j, num)
        )

    def solve(self):
        # Solve the Sudoku using backtracking
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] == 0:  # Empty cells have a 0 in them
                    for num in range(1, self.SIZE + 1):
                        if self.__check_num(i, j, num):
                            self.board[i][j] = num
                            if self.solve():
                                return True
                            else:
                                self.board[i][j] = 0  # Reset the cell if the solution is not valid
                    return False
        return True

