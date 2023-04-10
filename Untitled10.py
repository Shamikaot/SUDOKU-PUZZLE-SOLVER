#!/usr/bin/env python
# coding: utf-8

# In[1]:


def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using a backtracking algorithm.

    :param board: The Sudoku puzzle board, represented as a 9x9 list of integers.
    :return: True if the puzzle is solvable, False otherwise.
    """
    empty_pos = find_empty(board)
    if not empty_pos:
        return True

    row, col = empty_pos
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    """
    Finds the next empty position on the Sudoku puzzle board.

    :param board: The Sudoku puzzle board, represented as a 9x9 list of integers.
    :return: The row and column indices of the next empty position, or None if the board is full.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)

    return None


def is_valid(board, row, col, num):
    """
    Determines whether a number can be placed in a given position on the Sudoku puzzle board.

    :param board: The Sudoku puzzle board, represented as a 9x9 list of integers.
    :param row: The row index of the position to check.
    :param col: The column index of the position to check.
    :param num: The number to check.
    :return: True if the number can be placed in the given position, False otherwise.
    """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True


# In[ ]:





# In[ ]:




