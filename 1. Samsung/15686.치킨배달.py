from itertools import combinations

def chicken_distance(houses, candidate):
    total = 0
    for r1,c1 in houses:
        distance = 100
        for r2,c2 in candidate:
            distance = min(distance, abs(r1-r2) + abs(c1-c2))
        total += distance
    return total

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))

candidates = combinations(chickens, M)

answer = 10e9
for candidate in candidates:
    answer = min(answer, chicken_distance(houses, candidate))
print(answer)