from collections import deque

n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]

l = int(input())
drifts = dict()
for _ in range(l):
    x, c = input().split()
    drifts[int(x)] = c

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0
count = 0

queue = deque([[1,1]])
while True:
    if count in drifts:
        if drifts[count] == 'D':
            direction = (direction+1)%4
        else:
            direction = (direction-1)%4

    current = queue[-1]

    nx = current[1] + dx[direction]
    ny = current[0] + dy[direction]
    move = [ny, nx]
    count += 1

    if not(1 <= nx <= n) or not(1 <= ny <= n) or move in queue:
        break
    queue.append(move)

    if move in apples:
        apples.remove(move)
    else:
        queue.popleft()

print(count)