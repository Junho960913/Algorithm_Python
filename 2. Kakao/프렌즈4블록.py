def check_squares(x,y,board,remove):
    count = 0
    check = [[1,0], [0,1], [1,1]]
    for i in range(3):
        nx = x + check[i][0]
        ny = y + check[i][1]
        if board[y][x] and board[ny][nx] == board[y][x]:
            count += 1
    if count == 3:
        remove.append([x,y])
        for i in range(3):
            nx = x + check[i][0]
            ny = y + check[i][1]
            remove.append([nx,ny])
        
def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    
    while True:
        remove = []
        for i in range(m-1):
            for j in range(n-1):
                check_squares(j, i, board, remove)
        
        for x,y in remove:
            board[y][x] = 0
        
        print(1, board)
        while True:
            move = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and not board[i+1][j]:
                        move += 1
                        board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
            if not move:
                break
        print(2, board)
        if not remove:
            break
            
    for i in range(m):
        for j in range(n):
            if not board[i][j]:
                answer += 1
                    
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))