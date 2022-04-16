N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]


def DFS(r,c,connected):
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if L <= abs(countries[r][c]-countries[nr][nc]) <= R:
                visited[nr][nc] = True
                connected.append((nr,nc))
                DFS(nr,nc,connected)

def distribute(connected):
    total = 0
    for r,c in connected:
        total += countries[r][c]

    for r,c in connected:
        countries[r][c] = total//len(connected)

days = 0
while True:
    union = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                connected = [(i,j)]
                DFS(i,j,connected)
                if len(connected) > 1: ####### 이 부분 DFS 내에서 해결 가능?
                    union += 1
                    distribute(connected)
    if not union:
        break

    days += 1

print(days)

