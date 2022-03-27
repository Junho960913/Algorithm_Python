from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def up(board):
    for j in range(n):
        pointer1 = 0
        pointer2 = 1
        while pointer2 < n:
            if board[pointer1][j] == 0:
                if board[pointer2][j] != 0:
                    board[pointer1][j] = board[pointer2][j]
                    board[pointer2][j] = 0
                pointer2 += 1

            else:
                if board[pointer2][j] == 0:
                    pointer2 += 1
                elif board[pointer2][j] == board[pointer1][j]:
                    board[pointer1][j] *= 2
                    board[pointer2][j] = 0
                    pointer1 += 1
                    pointer2 += 1
                else:
                    pointer1 += 1
                    if pointer1 == pointer2:
                        pointer2 += 1

    return board

def down(board):
    for j in range(n):
        pointer1 = n-1
        pointer2 = n-2
        while pointer2 > -1:
            if board[pointer1][j] == 0:
                if board[pointer2][j] != 0:
                    board[pointer1][j] = board[pointer2][j]
                    board[pointer2][j] = 0
                pointer2 -= 1

            else:
                if board[pointer2][j] == 0:
                    pointer2 -= 1
                elif board[pointer2][j] == board[pointer1][j]:
                    board[pointer1][j] *= 2
                    board[pointer2][j] = 0
                    pointer1 -= 1
                    pointer2 -= 1
                else:
                    pointer1 -= 1
                    if pointer1 == pointer2:
                        pointer2 -= 1

    return board


def left(board):
    for i in range(n):
        pointer1 = 0
        pointer2 = 1
        while pointer2 < n:
            if board[i][pointer1] == 0:
                if board[i][pointer2] != 0:
                    board[i][pointer1] = board[i][pointer2]
                    board[i][pointer2] = 0
                pointer2 += 1

            else:
                if board[i][pointer2] == 0:
                    pointer2 += 1
                elif board[i][pointer2] == board[i][pointer1]:
                    board[i][pointer1] *= 2
                    board[i][pointer2] = 0
                    pointer1 += 1
                    pointer2 += 1
                else:
                    pointer1 += 1
                    if pointer1 == pointer2:
                        pointer2 += 1

    return board


def right(board):
    for i in range(n):
        pointer1 = n-1
        pointer2 = n-2
        while pointer2 > -1:
            if board[i][pointer1] == 0:
                if board[i][pointer2] != 0:
                    board[i][pointer1] = board[i][pointer2]
                    board[i][pointer2] = 0
                pointer2 -= 1

            else:
                if board[i][pointer2] == 0:
                    pointer2 -= 1
                elif board[i][pointer2] == board[i][pointer1]:
                    board[i][pointer1] *= 2
                    board[i][pointer2] = 0
                    pointer1 -= 1
                    pointer2 -= 1
                else:
                    pointer1 -= 1
                    if pointer1 == pointer2:
                        pointer2 -= 1

    return board

def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))

    else:
        return max(dfs(up(deepcopy(board)), cnt+1), dfs(down(deepcopy(board)), cnt+1), dfs(left(deepcopy(board)), cnt+1), dfs(right(deepcopy(board)), cnt+1))


print(up(board))