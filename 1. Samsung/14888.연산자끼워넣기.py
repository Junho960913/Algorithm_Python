n = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split())) # +, -, x, //

def dfs(depth, result, plus, minus, multi, div):
    if depth == n-1:
        return 

    else:
        dfs(depth+1, result, plus-1, minus, ) 
