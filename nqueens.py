def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else "-", end=" ")
        print()
    print()


def is_safe(row, col, left_diag, right_diag, col_check, n):
    return not (left_diag[row - col + n - 1] or 
                right_diag[row + col] or 
                col_check[col])


def solve_nqueen_util(board, row, n, left_diag, right_diag, col_check):
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(row, col, left_diag, right_diag, col_check, n):

            # Place queen
            board[row][col] = 1
            col_check[col] = True
            left_diag[row - col + n - 1] = True
            right_diag[row + col] = True

            # Recur for next row
            solve_nqueen_util(board, row + 1, n, left_diag, right_diag, col_check)

            # Backtrack
            board[row][col] = 0
            col_check[col] = False
            left_diag[row - col + n - 1] = False
            right_diag[row + col] = False


def solve_nqueen(n):
    board = [[0] * n for _ in range(n)]

    left_diag = [False] * (2 * n - 1)
    right_diag = [False] * (2 * n - 1)
    col_check = [False] * n

    solve_nqueen_util(board, 0, n, left_diag, right_diag, col_check)


# Driver code
n = 6
solve_nqueen(n)