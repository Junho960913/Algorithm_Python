n = int(input())
testers = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for room in range(n):
    if testers[room] <= b:
        answer += 1
    else:
        if (testers[room]-b)%c == 0:
            answer += (testers[room]-b)//c + 1
        else:
            answer += (testers[room]-b)//c + 2

print(answer)