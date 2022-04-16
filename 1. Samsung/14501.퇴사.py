n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    if i+schedule[i][0] <= n:
        dp[i] = max(dp[i+1], schedule[i][1]+dp[i+schedule[i][0]])
    else:
        dp[i] = dp[i+1]

print(max(dp))