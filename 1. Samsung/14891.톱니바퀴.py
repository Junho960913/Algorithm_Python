from collections import deque

status = [deque(map(int, input())) for _ in range(4)]
times = int(input())
rotates = [list(map(int, input().split())) for _ in range(times)]

def right(number, direction, status):
    if number == 4:
        return
    if status[number-1][2] != status[number][6]:
        right(number+1, -direction, status)
        status[number].rotate(direction)
    else:
        return

def left(number, direction, status):
    if number == -1:
        return
    if status[number+1][6] != status[number][2]:
        left(number-1, -direction, status)
        status[number].rotate(direction)
    else:
        return

answer = 0

for rotate in rotates:
    right(rotate[0], -rotate[1], status)
    left(rotate[0]-2, -rotate[1], status)
    status[rotate[0]-1].rotate(rotate[1])

for i in range(4):
    answer += (2**i)*status[i][0]

print(answer)