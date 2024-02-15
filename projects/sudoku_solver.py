"""
Program to solve a valid Sudoku puzzle.
The puzzle must be a 2D array of possible sudoku cells.
"""


def find_solutions(puzzle):
    pass


# verifies the puzzle's current state is valid
def verify_choice(puzzle):
    for i in range(9):
        for j in range(9):
            cell = puzzle[i][j]
            for k in range(9):
                if k == i:
                    continue
                if cell == puzzle[k][j]:
                    return False
            for k in range(9):
                if k == j:
                    continue
                if cell == puzzle[i][k]:
                    return False
    return True


def verify_solution(puzzle):
    if verify_choice(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return False
    else:
        return False
    return True


def make_sudoku():
    puzzle = [[0, 6, 0,  0, 0, 0,  3, 8, 0],
              [1, 0, 5,  0, 0, 0,  4, 0, 2],
              [3, 0, 4,  0, 0, 0,  0, 1, 0],

              [5, 0, 1,  6, 0, 2,  9, 4, 0],
              [0, 0, 9,  8, 3, 0,  2, 7, 5],
              [8, 2, 0,  0, 0, 0,  0, 0, 1],

              [2, 0, 0,  3, 0, 0,  7, 5, 0],
              [0, 0, 0,  2, 0, 0,  1, 0, 9],
              [4, 9, 6,  1, 0, 7,  0, 2, 0]
              ]
    return puzzle


def print_sudoku(sudoku):
    for i in range(9):
        text = ""
        for j in range(9):
            text = text + str(sudoku[i][j]) + " "
            if j == 2 or j == 5:
                text = text + " "
        if i == 3 or i == 6:
            print()
        print(text)


find_solutions(make_sudoku())
