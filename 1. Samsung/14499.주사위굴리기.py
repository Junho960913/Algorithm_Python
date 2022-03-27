n, m, y, x, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
queries = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
flag = 0

# 0: 위, 1: 앞, 2: 아래, 3: 뒤, 4: 왼, 5:오른
def down(dice):
    dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]

def up(dice):
    dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

def left(dice):
    dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]

def right(dice):
    dice[0], dice[5], dice[2], dice[4] = dice[4], dice[0], dice[5], dice[2]

def update(board, dice, nx, ny):
    if board[ny][nx] == 0:
        board[ny][nx] = dice[2]
    else:
        dice[2] = board[ny][nx]
        board[ny][nx] = 0
    print(dice[0])

for query in queries:
    if query == 1: # 동
        dx, dy = 1, 0
        if 0 <= x+dx < m and 0 <= y+dy < n:
            right(dice)
            x += dx
            y += dy
            update(board, dice, x, y)

    elif query == 2: # 서
        dx, dy = -1, 0
        if 0 <= x+dx < m and 0 <= y+dy < n:
            left(dice)
            x += dx
            y += dy
            update(board, dice, x, y)

    elif query == 3: # 북
        dx, dy = 0, -1
        if 0 <= x+dx < m and 0 <= y+dy < n:
            up(dice)
            x += dx
            y += dy
            update(board, dice, x, y)

    elif query == 4: # 남
        dx, dy = 0, 1
        if 0 <= x+dx < m and 0 <= y+dy < n:
            down(dice)
            x += dx
            y += dy
            update(board, dice, x, y)