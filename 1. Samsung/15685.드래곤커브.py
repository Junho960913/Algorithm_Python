N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]

def make_dragon(x,y,d,g):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    moves = [(x,y),(x+dx[d],y+dy[d])]
    for _ in range(g):
        length = len(moves)
        for i in range(length-2,-1,-1):
            nx = moves[i+1][1] - moves[i][1]
            ny = moves[i][0] - moves[i+1][0]
            move = (moves[-1][0]+nx, moves[-1][1]+ny)
            moves.append(move)
    return moves

total = []
for x,y,d,g in infos:
    move = make_dragon(x,y,d,g)
    total += move


total = set(total)
answer = 0
for i in range(100):
    for j in range(100):
        count = 0
        checks = [[0,0],[1,0],[0,1],[1,1]]
        for k in range(4):
            if (i+checks[k][0],j+checks[k][1]) in total:
                count += 1
        if count == 4:
            answer += 1
print(answer)