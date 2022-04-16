from copy import deepcopy
from itertools import combinations
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
board = []
zeros = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if not row[j]:
            zeros.append((i, j))
    board.append(row)

def DFS(board, y, x):
    visited = [[False]*m for _ in range(n)]
    visited[y][x] = True
    stack = [(y,x)]
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and not board[ny][nx]:
                    visited[ny][nx] = True
                    board[ny][nx] = 2
                    stack.append((ny,nx))

def Count(board):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                DFS(board, i, j)
    count = 0
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                count += 1
    return count

test_cases = combinations(zeros, 3)
answer = 0
for test_case in test_cases:
    test_board = deepcopy(board)
    for i, j in test_case:
        test_board[i][j] = 1
    answer = max(answer, Count(test_board))

print(answer)
