from collections import defaultdict

N, M, K = map(int, input().split())
land_current = [[5]*N for _ in range(N)]
land_add = [list(map(int, input().split())) for _ in range(N)]
trees = defaultdict(list)
trees_dead = defaultdict(list)
trees_add = defaultdict(list)
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[(r,c)].append(age)

def spring():
    for i in trees:
        trees[i].sort()

    for coords in trees:
        count = 0
        for age in trees[coords]:
            if land_current[coords[0]-1][coords[1]-1] >= age:
                land_current[coords[0]-1][coords[1]-1] -= age
                count += 1
            else:
                trees_dead[coords] += trees[coords][count:]
                trees[coords] = trees[coords][:count]
                break
        trees[coords] = [x+1 for x in trees[coords]]

def summer():
    global trees_dead
    for coords in trees_dead:
        for age in trees_dead[coords]:
            land_current[coords[0]-1][coords[1]-1] += age//2
    trees_dead = defaultdict(list)

def fall():
    global trees_add
    for coords in trees:
        for age in trees[coords]:
            if age%5 == 0:
                dr = [-1,-1,-1,0,0,+1,+1,+1]
                dc = [-1,0,+1,-1,+1,-1,0,+1]
                for i in range(8):
                    nr = coords[0] + dr[i]
                    nc = coords[1] + dc[i]
                    if 1 <= nr <= N and 1 <= nc <= N:
                        trees_add[(nr,nc)].append(1)
    for coords in trees_add:
        trees[coords] += trees_add[coords]
    trees_add = defaultdict(list)

def winter():
    for i in range(N):
        for j in range(N):
            land_current[i][j] += land_add[i][j]

for _ in range(K):
    spring()
    summer()
    fall()
    winter()
    
total = 0
for coords in trees:
    total += len(trees[coords])

print(total)