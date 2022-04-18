from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            current = (i,j)

def BFS(r,c,size):
    stack = deque([(r,c,0)])
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True
    candidate = []
    time_check = 0
    while stack:
        current = stack.popleft()
        dr = [-1,0,0,1]
        dc = [0,-1,1,0]
        for i in range(4):
            nr = current[0] + dr[i]
            nc = current[1] + dc[i]
            time = current[2] + 1
            move = (nr,nc,time)

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                if size >= board[nr][nc]:
                    if board[nr][nc] and size > board[nr][nc]:
                        candidate.append(move)

                    else:
                        stack.append(move)

    if candidate:
        return sorted(candidate, key=lambda x: [x[2],x[0],x[1]])[0]
    else:
        return False

answer = 0
size = 2
eat = 0

while True:
    r, c = current[0], current[1]
    current = BFS(r, c, size)
    if current:
        board[r][c] = 0
        board[current[0]][current[1]] = 9
        eat += 1
        answer += current[2]
        if size == eat:
            size += 1
            eat = 0
    else:
        print(answer)
        break
