p_board = [[0, 6, 0, 3, 0, 0, 8, 0, 4],
           [5, 3, 7, 0, 9, 0, 0, 0, 0],
           [0, 4, 0, 0, 0, 6, 3, 0, 7],
           [0, 9, 0, 0, 5, 1, 2, 3, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [7, 1, 3, 6, 2, 0, 0, 4, 0],
           [3, 0, 6, 4, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 6, 0, 5, 2, 3],
           [1, 0, 2, 0, 0, 9, 0, 8, 0]]


def print_board(board):
    """""
    Prints the board to the console using for loops
    :param board: 2d list of ints, sudoku board
    """""
    for rows in board:
        print(*rows)


def get_row(board, r):
    """
    returns desired row as a list
    :param board: 9 x 9 sudoku board
    :param r: desired row
    :return: list of values in the row
    """
    row = board[r]
    return row


def get_col(board, c):
    """
    returns desired column as a list
    :param board: 9 x 9 sudoku board
    :param c: desired column
    :return: list of values in the column
    """
    column = []
    for x in range(9):
        column.append(board[x][c])
    return column


def get_box(board, r, c):
    """
    returns the values of a 3 x 3 box about the top left coord
    :param board: 9 x 9 sudoku board
    :param r: desired row
    :param c: desired column
    :return: list of values in the box
    """
    box = []
    # set r,c to 1 of 9 boxes
    if r in range(0, 3):
        r = 0
    elif r in range(3, 6):
        r = 3
    elif r in range(6, 10):
        r = 6

    if c in range(0, 3):
        c = 0
    elif c in range(3, 6):
        c = 3
    elif c in range(6, 10):
        c = 6

    for x in range(3):
        for y in range(3):
            box.append(board[r + x][c + y])
    return box


def verify(board, r, c, guess):
    """
    verify if guess at (r,c) is in the associated row, col or quadrant
    :param board: 9 x 9 sudoku board
    :param r: row coord
    :param c: col coord
    :param guess: current guess
    :return: True if guess is not found, False if guess is found
    """
    if guess in get_row(board, r):
        return False
    elif guess in get_col(board, c):
        return False
    elif guess in get_box(board, r, c):
        return False
    else:
        return True


def find_zero(board):
    """""
    Parses through the board until a zero is found
    :param board: 2d list of ints, sudoku board
    :return: x coordinate
    :return: y coordinate
    """""
    for i in range(9):
        for j in range(9):
            # print('Row:', row, 'Col:', column, 'Value:', sub_list)
            if board[i][j] == 0:
                return i, j
    return None


def solve(board):
    """
    backtracking algorithm to solve sudoku board
    try a value, then verify. if we run out of values the function
    will return to the previous blank spot and try the rest of the values
    :param board: 3 x 3 sudoku board
    :return: True when solver succeeds, false when we run out of values
    """
    find = find_zero(board)

    if not find_zero(board):
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if verify(board, row, col, i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


def main():
    print_board(p_board)
    solve(p_board)
    print('___________________')
    print_board(p_board)


if __name__ == '__main__':main()
