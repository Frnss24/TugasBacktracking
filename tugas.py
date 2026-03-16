import time

N = 8  # Papan

board = [[0 for _ in range(N)] for _ in range(N)]

def print_board():
    print("\n")
    for row in board:
        for col in row:
            if col == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\n")
    time.sleep(0.3)


def is_safe(row, col):

    # cek kolom
    for i in range(row):
        if board[i][col] == 1:
            return False

    # cek diagonal kiri
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # cek diagonal kanan
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):

    if row == N:
        print("SOLUSI DITEMUKAN")
        print_board()
        return True

    for col in range(N):

        if is_safe(row, col):

            board[row][col] = 1
            print(f"Menaruh Queen di ({row},{col})")
            print_board()

            if solve(row + 1):
                return True

            board[row][col] = 0
            print(f"Backtracking dari ({row},{col})")
            print_board()

    return False


solve(0)